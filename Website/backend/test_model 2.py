import torch
import os

print("Step 1: Finding model file...")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
possible_names = ['ConvNextmodel.pth', 'convnextmodel.pth', 'ConvNext_model.pth']

model_path = None
for name in possible_names:
    test_path = os.path.join(BASE_DIR, name)
    if os.path.exists(test_path):
        model_path = test_path
        print(f"✓ Found: {name}")
        break

if not model_path:
    print("❌ Model file not found!")
    exit()

print("\nStep 2: Loading checkpoint...")
checkpoint = torch.load(model_path, map_location='cpu')

print("\nStep 3: Checkpoint structure:")
if isinstance(checkpoint, dict):
    print(f"  Type: Dictionary with keys: {list(checkpoint.keys())}")
else:
    print(f"  Type: {type(checkpoint)}")

print("\n✓ Model loads without crashing!")
