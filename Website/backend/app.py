import gradio as gr
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import os

# Get model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Try different possible filenames
possible_names = ['ConvNextmodel.pth', 'convnextmodel.pth', 'ConvNext_model.pth']
model_path = None

for name in possible_names:
    test_path = os.path.join(BASE_DIR, name)
    if os.path.exists(test_path):
        model_path = test_path
        print(f"✓ Found model: {name}")
        break

if model_path is None:
    raise FileNotFoundError(f"Could not find model file. Tried: {possible_names}")

# Species categories (7 classes)
SPECIES_CATEGORIES = [
    'Sea Star',
    'Sea Urchin',
    'Sea Anemone',
    'Sea Cucumber',
    'Crab',
    'Coral',
    'Sponge'
]

# Load model
print(f"Loading model from: {model_path}")
model = AutoModelForImageClassification.from_pretrained(
    'facebook/convnext-tiny-224',
    num_labels=7,
    ignore_mismatched_sizes=True
)

# Load weights
checkpoint = torch.load(model_path, map_location='cpu')
if isinstance(checkpoint, dict):
    if 'model' in checkpoint:
        checkpoint = checkpoint['model']
    elif 'state_dict' in checkpoint:
        checkpoint = checkpoint['state_dict']

model.load_state_dict(checkpoint, strict=False)
model.eval()

# Load processor
processor = AutoImageProcessor.from_pretrained('facebook/convnext-tiny-224')
print("✓ Model loaded successfully!")

def classify_image(image):
    """
    Classify a benthic species image.
    
    Args:
        image: PIL Image or numpy array
    
    Returns:
        dict: Predictions with species names and confidence scores
    """
    # Convert to PIL if needed
    if not isinstance(image, Image.Image):
        image = Image.fromarray(image).convert('RGB')
    
    # Preprocess
    inputs = processor(images=image, return_tensors="pt")
    
    # Predict
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.nn.functional.softmax(logits, dim=1)
    
    # Create results dictionary for Gradio
    results = {}
    for idx, prob in enumerate(probabilities[0]):
        results[SPECIES_CATEGORIES[idx]] = float(prob)
    
    return results

# Create Gradio interface
demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil", label="Upload Underwater Image"),
    outputs=gr.Label(num_top_classes=7, label="Species Classification"),
    title="BenthicAI - Benthic Species Classifier",
    description="Upload an image of a benthic organism to classify it into one of 7 species categories. Built with ConvNeXT transformer model.",
    examples=[
        ["examples/seastar.jpg"],
        ["examples/urchin.jpg"],
        ["examples/coral.jpg"],
    ] if os.path.exists("examples") else None,
    theme=gr.themes.Soft(),
    allow_flagging="never"
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False  # Set to True to get a public URL
    )
