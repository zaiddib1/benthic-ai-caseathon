import sys
print(f"Python: {sys.version}")

print("\nTesting imports...")

try:
    import torch
    print(f"✓ torch {torch.__version__}")
except Exception as e:
    print(f"✗ torch failed: {e}")
    exit(1)

try:
    import torchvision
    print(f"✓ torchvision {torchvision.__version__}")
except Exception as e:
    print(f"✗ torchvision failed: {e}")

try:
    import transformers
    print(f"✓ transformers {transformers.__version__}")
except Exception as e:
    print(f"✗ transformers failed: {e}")
    exit(1)

print("\nTesting transformers import...")
try:
    from transformers import AutoModelForImageClassification
    print("✓ AutoModelForImageClassification imported")
except Exception as e:
    print(f"✗ Failed: {e}")
    exit(1)

print("\nAll imports successful!")
