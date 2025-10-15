import gradio as gr
from PIL import Image

def classify_image(image):
    """Simple test without loading the heavy model first"""
    return {
        "Sea Star": 0.8,
        "Sea Urchin": 0.1,
        "Coral": 0.05,
        "Crab": 0.03,
        "Sea Anemone": 0.01,
        "Sponge": 0.005,
        "Sea Cucumber": 0.005
    }

demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=7),
    title="BenthicAI Classifier (Test)"
)

if __name__ == "__main__":
    demo.launch(server_port=7860)
