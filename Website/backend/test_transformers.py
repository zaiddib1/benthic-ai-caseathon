import torch
from transformers import AutoModelForImageClassification
import os

print("=" * 60)
print("Step 1: Finding model file...")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = None
for name in ['ConvNextmodel.pth', 'convnextmodel.pth']:
    test_path = os.path.join(BASE_DIR, name)
    if os.path.exists(test_path):
        model_path = test_path
        print(f"✓ Found: {name}")
        break

if not model_path:
    print("❌ No model file found!")
    exit(1)

print(f"File size: {os.path.getsize(model_path) / (1024*1024):.2f} MB")

print("\n" + "=" * 60)
print("Step 2: Loading base model architecture...")
try:
    model = AutoModelForImageClassification.from_pretrained(
        'facebook/convnext-tiny-224',
        num_labels=7,
        ignore_mismatched_sizes=True
    )
    print("✓ Base model loaded")
except Exception as e:
    print(f"❌ Failed to load base model: {e}")
    exit(1)

print("\n" + "=" * 60)
print("Step 3: Loading checkpoint...")
try:
    checkpoint = torch.load(model_path, map_location='cpu', weights_only=False)
    print(f"✓ Checkpoint loaded - type: {type(checkpoint)}")
except Exception as e:
    print(f"❌ Failed to load checkpoint: {e}")
    exit(1)

print("\n" + "=" * 60)
print("Step 4: Extracting state_dict...")
if isinstance(checkpoint, dict):
    print(f"Checkpoint keys: {list(checkpoint.keys())}")
    if 'model' in checkpoint:
        checkpoint = checkpoint['model']
        print("  Using checkpoint['model']")
    elif 'state_dict' in checkpoint:
        checkpoint = checkpoint['state_dict']
        print("  Using checkpoint['state_dict']")
    else:
        print("  Using checkpoint directly")

print(f"State dict has {len(checkpoint)} keys")

print("\n" + "=" * 60)
print("Step 5: Loading weights into model...")
try:
    incompatible_keys = model.load_state_dict(checkpoint, strict=False)
    print("✓ Weights loaded")
    if incompatible_keys.missing_keys:
        print(f"  Missing keys: {len(incompatible_keys.missing_keys)}")
    if incompatible_keys.unexpected_keys:
        print(f"  Unexpected keys: {len(incompatible_keys.unexpected_keys)}")
except Exception as e:
    print(f"❌ Failed to load weights: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

print("\n" + "=" * 60)
print("Step 6: Setting eval mode...")
model.eval()
print("✓ Model in eval mode")

print("\n" + "=" * 60)
print("✓✓✓ MODEL LOADED SUCCESSFULLY! ✓✓✓")
print(f"Model has {sum(p.numel() for p in model.parameters()):,} parameters")
print("=" * 60)
