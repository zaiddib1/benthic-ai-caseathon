import os
from typing import List, Dict, Any
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx

HF_CLASSIFY_URL = os.getenv("HF_CLASSIFY_URL", "")   # e.g. https://xxxx.endpoints.huggingface.cloud
HF_DETECT_URL   = os.getenv("HF_DETECT_URL", "")
HF_TOKEN        = os.getenv("HF_TOKEN", "")          # Bearer token for your endpoint(s)

TIMEOUT = httpx.Timeout(60.0, connect=10.0)
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"} if HF_TOKEN else {}

app = FastAPI(title="Benthic API")

# CORS for your Vue app origin(s)
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ALLOW_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthz")
def health():
    return {"ok": True}

async def _post_inference(url: str, img: UploadFile, extra_json: Dict[str, Any] | None = None):
    if not url:
        raise HTTPException(status_code=500, detail="Model endpoint URL not configured")
    # Some endpoints accept raw image bytes; some expect JSON {inputs: base64}; adjust if needed
    # This version sends raw bytes as body (common pattern for HF image endpoints).
    data = await img.read()
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        # Prefer sending bytes with appropriate content-type
        headers = {"Content-Type": img.content_type or "application/octet-stream", **HEADERS}
        r = await client.post(url, content=data, headers=headers, params=extra_json or {})
        if r.status_code >= 400:
            raise HTTPException(status_code=r.status_code, detail=r.text)
        try:
            return r.json()
        except Exception:
            return {"raw": r.text}

@app.post("/classify")
async def classify(files: List[UploadFile] = File(...)) -> Dict[str, Any]:
    """
    Accepts 1..N images and returns an array of per-image predictions.
    """
    results = []
    for f in files:
        out = await _post_inference(HF_CLASSIFY_URL, f)
        # Normalize common formats:
        # - HF image-classification: list of {label, score}
        # - custom: wrap as-is
        if isinstance(out, list) and out and isinstance(out[0], dict) and "label" in out[0]:
            norm = [{"species": x.get("label"), "confidence": float(x.get("score", 0))} for x in out]
            results.append({"filename": f.filename, "predictions": norm})
        else:
            results.append({"filename": f.filename, "predictions": out})
    return {"results": results}

@app.post("/detect")
async def detect(
    files: List[UploadFile] = File(...),
    conf: float = Form(0.25),
    iou: float = Form(0.45),
) -> Dict[str, Any]:
    """
    Accepts 1..N images; returns detections per image.
    Passes thresholds as query params (?conf=...&iou=...) to your model endpoint.
    """
    results = []
    for f in files:
        out = await _post_inference(HF_DETECT_URL, f, {"conf": conf, "iou": iou})
        # Normalize a common yolov5/8 style response if present
        # Expecting something like: [{"bbox":[x,y,w,h], "label":"Skate", "score":0.92}, ...]
        detections = []
        if isinstance(out, list):
            for d in out:
                bbox = d.get("bbox") or d.get("box") or {}
                detections.append({
                    "species": d.get("label") or d.get("class") or "Unknown",
                    "confidence": float(d.get("score", 0)),
                    "bbox": {
                        "x": bbox.get("x") or bbox[0] if isinstance(bbox, list) and len(bbox) > 0 else 0,
                        "y": bbox.get("y") or bbox[1] if isinstance(bbox, list) and len(bbox) > 1 else 0,
                        "width":  bbox.get("width")  or bbox[2] if isinstance(bbox, list) and len(bbox) > 2 else 0,
                        "height": bbox.get("height") or bbox[3] if isinstance(bbox, list) and len(bbox) > 3 else 0,
                    }
                })
        results.append({"filename": f.filename, "detections": detections or out})
    return {"results": results}
