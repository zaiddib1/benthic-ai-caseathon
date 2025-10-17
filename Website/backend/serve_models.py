# backend/serve_models.py
# LitServe backend with:
#  - AutoModelForImageClassification + AutoImageProcessor (convnext)
#  - ultralytics.YOLO (dshi01/yoloUW)
#  - Single /predict supporting 'mode' (Option A)
#  - PLUS convenience routes /classify and /detect (Option B)
#  - CORS for your Quasar app

import io
import os
import base64
from typing import List, Dict, Any

from PIL import Image
import torch
from fastapi.middleware.cors import CORSMiddleware

import litserve as ls
from transformers import AutoModelForImageClassification, AutoImageProcessor
from ultralytics import YOLO
from huggingface_hub import hf_hub_download, list_repo_files

def _load_ultralytics_from_hf(repo_id: str, filename: str | None = None) -> YOLO:
    """
    Download a .pt weight from Hugging Face and load with Ultralytics YOLO.
    If filename is None, try common names, then fall back to the first .pt in repo.
    """
    # If the user provided an explicit filename via env, prefer it
    if filename:
        weight_path = hf_hub_download(repo_id=repo_id, filename=filename)
        return YOLO(weight_path)

    # Try common YOLO weight names
    candidates = (
        "yolo11_150_best.pt",
        "weights/best.pt",
        "model.pt",
        "yolov8n.pt",
        "yolov8s.pt",
    )
    for fname in candidates:
        try:
            weight_path = hf_hub_download(repo_id=repo_id, filename=fname)
            return YOLO(weight_path)
        except Exception:
            pass  # try next

    # As a last resort, list repo files and pick the first .pt
    files = list_repo_files(repo_id)
    pt_files = [f for f in files if f.lower().endswith(".pt")]
    if not pt_files:
        raise FileNotFoundError(
            f"No .pt weights found in HF repo '{repo_id}'. "
            "Set DET_FILENAME env var to the correct file name."
        )
    weight_path = hf_hub_download(repo_id=repo_id, filename=pt_files[0])
    return YOLO(weight_path)

def _decode_base64_images(b64_list: List[str]) -> List[Image.Image]:
    images: List[Image.Image] = []
    for b64 in b64_list:
        img_bytes = base64.b64decode(b64)
        img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        images.append(img)
    return images


class VisionAPI(ls.LitAPI):
    """
    POST /predict
      { mode: "classify"|"detect", images: [base64...], top_k?, conf_threshold?, iou_threshold? }
    PLUS helper routes (Option B):
    POST /classify
      { images: [base64...], top_k? }
    POST /detect
      { images: [base64...], conf_threshold?, iou_threshold? }
    """

    def setup(self, device: torch.device):
        self.device = device

        # ---- Classification (HF Auto classes)
        clf_repo = os.getenv("CLF_REPO", "dshi01/convnext-tiny-224-7clss")
        self.processor = AutoImageProcessor.from_pretrained(clf_repo)
        self.clf_model = AutoModelForImageClassification.from_pretrained(clf_repo)
        self.clf_model.to('cpu').eval()
        self.id2label = {int(k): v for k, v in (self.clf_model.config.id2label or {}).items()}

        # ---- Detection (Ultralytics)
        det_repo = os.getenv("DET_REPO", "dshi01/yoloUW")
        det_filename=('yolo11_150_best.pt')
        self.det_model = _load_ultralytics_from_hf(det_repo, det_filename)
        self.det_model.to('cpu')

    # ---------- Core LitServe contract ----------
    def decode_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        mode = request.get("mode", "classify")
        if mode not in ("classify", "detect"):
            raise ValueError("mode must be 'classify' or 'detect'")

        images_b64 = request["images"]
        images = _decode_base64_images(images_b64)

        top_k = int(request.get("top_k", 3))
        conf_threshold = float(request.get("conf_threshold", 0.25))
        iou_threshold = float(request.get("iou_threshold", 0.45))

        return {
            "mode": mode,
            "images": images,
            "top_k": top_k,
            "conf_threshold": conf_threshold,
            "iou_threshold": iou_threshold,
        }

    def predict(self, payload: Dict[str, Any]) -> List[Any]:
        if payload["mode"] == "classify":
            return self._predict_classify(payload["images"], payload["top_k"])
        return self._predict_detect(
            payload["images"],
            conf=payload["conf_threshold"],
            iou=payload["iou_threshold"],
        )

    def encode_response(self, output: List[Any]) -> Dict[str, Any]:
        return {"predictions": output}
    # -------------------------------------------

    # ---------- Shared task logic ----------
    def _predict_classify(self, images: List[Image.Image], top_k: int) -> List[Dict[str, Any]]:
        inputs = self.processor(images=images, return_tensors="pt")
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        with torch.no_grad():
            logits = self.clf_model(**inputs).logits
            probs = torch.nn.functional.softmax(logits, dim=-1)
        topk = torch.topk(probs, k=min(top_k, probs.shape[-1]), dim=-1)
        idxs = topk.indices.cpu().tolist()
        vals = topk.values.cpu().tolist()

        outs = []
        for lbls, scs in zip(idxs, vals):
            outs.append({
                "task": "classification",
                "top_k": [
                    {
                        "label": self.id2label.get(i, str(i)),
                        "index": i,
                        "score": float(s)
                     } for i, s in zip(lbls, scs)
                ]
            })
        return outs

    def _predict_detect(self, images: List[Image.Image], conf: float, iou: float) -> List[Dict[str, Any]]:
        outs: List[Dict[str, Any]] = []
        for img in images:
            res = self.det_model.predict(
                source=img,
                conf=conf,
                iou=iou,
                verbose=False,
                device='cpu'
            )[0]
            W, H = img.size
            dets = []
            if res.boxes is not None and len(res.boxes) > 0:
                xyxy = res.boxes.xyxy.cpu().tolist()
                confs = res.boxes.conf.cpu().tolist()
                clss  = res.boxes.cls.cpu().tolist()
                names = getattr(self.det_model.model, "names", None) or getattr(res, "names", None) or {}
                for (x1,y1,x2,y2), sc, c in zip(xyxy, confs, clss):
                    dets.append({
                        "bbox_xyxy": [float(x1), float(y1), float(x2), float(y2)],
                        "bbox_norm_xyxy": [x1/W, y1/H, x2/W, y2/H],
                        "score": float(sc),
                        "label": names.get(int(c), str(int(c))),
                        "class_index": int(c)
                    })
            outs.append({"task": "detection", "detections": dets})
        return outs
    # --------------------------------------

# ---------------- Boot the server, add friendly routes ----------------
if __name__ == "__main__":
    api = VisionAPI()
    server = ls.LitServer(api, accelerator="cpu")

    # Ensure the API is initialized (models/processors loaded) so helper routes
    # that call api._predict_classify/_predict_detect can run outside the
    # LitServer request loop. LitServer will also call setup when starting
    # normally, but we call it here to avoid AttributeError in synchronous
    # route handlers registered below.
    try:
        api.setup(torch.device('cpu'))
    except Exception:
        # If setup fails here, let server.run() attempt normal startup and
        # surface errors. We don't want to swallow exceptions silently.
        raise

    # Optional strict CORS
    origins = os.getenv("CORS_ALLOW_ORIGINS")  # e.g., "http://localhost:9000,https://your.site"
    if origins:
        # split comma-separated origins and strip whitespace
        allow_origins = [o.strip() for o in origins.split(",") if o.strip()]
        if allow_origins:
            server.app.add_middleware(
                CORSMiddleware,
                allow_origins=allow_origins,
                allow_credentials=False,
                allow_methods=["*"],
                allow_headers=["*"],
            )

    # ----- Option B: convenience routes that call the same logic -----
    @server.app.post("/classify")
    async def classify_route(payload: Dict[str, Any]):
        # expects { images: [base64...], top_k? }
        images = _decode_base64_images(payload["images"])
        top_k = int(payload.get("top_k", 3))
        return {"predictions": api._predict_classify(images, top_k)}

    @server.app.post("/detect")
    async def detect_route(payload: Dict[str, Any]):
        # expects { images: [base64...], conf_threshold?, iou_threshold? }
        images = _decode_base64_images(payload["images"])
        conf = float(payload.get("conf_threshold", 0.25))
        iou  = float(payload.get("iou_threshold", 0.45))
        return {"predictions": api._predict_detect(images, conf, iou)}
    # -----------------------------------------------------------------

    port = int(os.getenv("PORT", "8000"))
    server.run(port=port)
