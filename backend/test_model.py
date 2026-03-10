"""
test_model.py — Evaluate the trained crop disease model on held-out test images.

Usage:
    python test_model.py

The script samples a portion of images from each class in the dataset (unused
during training due to the 80/20 split) and reports per-class and overall accuracy.
"""
import os
import sys
import random
import numpy as np
from PIL import Image
from collections import defaultdict

# ── Config ────────────────────────────────────────────────────────────────────
DATASET_DIR = "dataset"
MODEL_PATH  = "crop_disease_model.h5"
LABELS_PATH = "labels.txt"
IMG_SIZE    = (224, 224)
SAMPLE_SIZE = 10   # images to test per class (pick last N to simulate test split)

# ── Load TensorFlow ───────────────────────────────────────────────────────────
try:
    import tensorflow as tf
except ImportError:
    print("❌ TensorFlow is not installed. Run: pip install tensorflow")
    sys.exit(1)


def load_labels(path: str) -> list:
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]


def preprocess(image_path: str) -> np.ndarray:
    img = Image.open(image_path).convert("RGB").resize(IMG_SIZE)
    arr = np.array(img) / 255.0
    return np.expand_dims(arr, axis=0)


def main():
    # ── Validate paths ────────────────────────────────────────────────────────
    if not os.path.exists(MODEL_PATH):
        print(f"❌ Model not found at '{MODEL_PATH}'. Run train.py first.")
        sys.exit(1)
    if not os.path.exists(LABELS_PATH):
        print(f"❌ Labels file not found at '{LABELS_PATH}'. Run train.py first.")
        sys.exit(1)
    if not os.path.exists(DATASET_DIR):
        print(f"❌ Dataset directory '{DATASET_DIR}' not found.")
        sys.exit(1)

    print(f"📦 Loading model from {MODEL_PATH} ...")
    model = tf.keras.models.load_model(MODEL_PATH)

    labels = load_labels(LABELS_PATH)
    label_to_idx = {lbl: i for i, lbl in enumerate(labels)}

    print(f"🏷️  Classes: {len(labels)}")
    print(f"🔬 Sampling {SAMPLE_SIZE} images per class for evaluation\n")

    # ── Evaluate ──────────────────────────────────────────────────────────────
    correct_total = 0
    tested_total  = 0
    per_class_results = []

    class_dirs = sorted([
        d for d in os.listdir(DATASET_DIR)
        if os.path.isdir(os.path.join(DATASET_DIR, d))
    ])

    for class_name in class_dirs:
        true_idx = label_to_idx.get(class_name)
        if true_idx is None:
            print(f"  ⚠️  Skipping '{class_name}' (not in labels)")
            continue

        class_path = os.path.join(DATASET_DIR, class_name)
        image_files = [
            os.path.join(class_path, f)
            for f in os.listdir(class_path)
            if f.lower().endswith((".jpg", ".jpeg", ".png"))
        ]

        # Use the last SAMPLE_SIZE images (simulating a hold-out test set)
        test_images = image_files[-SAMPLE_SIZE:] if len(image_files) >= SAMPLE_SIZE else image_files
        if not test_images:
            continue

        correct_class = 0
        for img_path in test_images:
            try:
                arr = preprocess(img_path)
                preds = model.predict(arr, verbose=0)
                predicted_idx   = int(np.argmax(preds[0]))
                predicted_label = labels[predicted_idx] if predicted_idx < len(labels) else "?"
                confidence      = float(np.max(preds[0]))

                if predicted_idx == true_idx:
                    correct_class += 1
            except Exception as e:
                print(f"    ⚠️  Could not process {img_path}: {e}")

        acc = correct_class / len(test_images) * 100
        per_class_results.append((class_name, correct_class, len(test_images), acc))
        correct_total += correct_class
        tested_total  += len(test_images)

    # ── Report ────────────────────────────────────────────────────────────────
    print("=" * 70)
    print(f"{'CLASS':<45} {'CORRECT':>7} {'TOTAL':>5} {'ACC':>6}")
    print("-" * 70)
    for cls, correct, total, acc in per_class_results:
        emoji = "✅" if acc >= 60 else "⚠️ " if acc >= 40 else "❌"
        short = cls[:42] + "..." if len(cls) > 42 else cls
        print(f"{emoji} {short:<44} {correct:>7} {total:>5} {acc:>5.1f}%")

    print("=" * 70)
    overall = correct_total / max(tested_total, 1) * 100
    print(f"\n🎯 Overall Accuracy : {overall:.1f}%  ({correct_total}/{tested_total})")
    print(f"📊 Classes tested   : {len(per_class_results)}")

    if overall >= 70:
        print("\n🟢 Model performance is GOOD — ready for production!")
    elif overall >= 50:
        print("\n🟡 Model performance is MODERATE — consider training more epochs.")
    else:
        print("\n🔴 Model performance is LOW — retrain with more data/epochs.")


if __name__ == "__main__":
    main()
