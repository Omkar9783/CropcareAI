import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from model import create_model

# ── Configuration ──────────────────────────────────────────────────────────────
DATASET_DIR = "dataset"
IMG_SIZE    = (224, 224)
BATCH_SIZE  = 32
EPOCHS      = 10        # Training up to 10 epochs; EarlyStopping will halt earlier if needed
MODEL_OUT   = "crop_disease_model.h5"
LABELS_OUT  = "labels.txt"


def prepare_data(data_dir: str):
    """
    Build train + validation generators from the PlantVillage dataset directory.
    Uses 80/20 split with augmentation on the training set.
    """
    train_datagen = ImageDataGenerator(
        rescale=1.0 / 255,
        rotation_range=25,
        width_shift_range=0.15,
        height_shift_range=0.15,
        shear_range=0.15,
        zoom_range=0.15,
        horizontal_flip=True,
        brightness_range=[0.8, 1.2],
        fill_mode="nearest",
        validation_split=0.2,
    )

    val_datagen = ImageDataGenerator(
        rescale=1.0 / 255,
        validation_split=0.2,
    )

    train_gen = train_datagen.flow_from_directory(
        data_dir,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="training",
        shuffle=True,
    )

    val_gen = val_datagen.flow_from_directory(
        data_dir,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="validation",
        shuffle=False,
    )

    return train_gen, val_gen


def train():
    # 1. Ensure dataset exists
    if not os.path.exists(DATASET_DIR):
        print("Dataset folder not found. Running copy_subset.py to download a subset...")
        os.system("python copy_subset.py")

    # 2. Prepare data generators
    print("\n📂 Loading dataset from:", DATASET_DIR)
    train_gen, val_gen = prepare_data(DATASET_DIR)
    num_classes = train_gen.num_classes
    print(f"   Classes found : {num_classes}")
    print(f"   Training imgs : {train_gen.samples}")
    print(f"   Validation imgs: {val_gen.samples}")

    # 3. Build model
    print("\n🔧 Building MobileNetV2 model...")
    model = create_model(num_classes)

    # 4. Callbacks
    callbacks = [
        EarlyStopping(
            monitor="val_accuracy",
            patience=3,
            restore_best_weights=True,
            verbose=1,
        ),
        ModelCheckpoint(
            filepath=MODEL_OUT,
            monitor="val_accuracy",
            save_best_only=True,
            verbose=1,
        ),
        ReduceLROnPlateau(
            monitor="val_loss",
            factor=0.5,
            patience=2,
            min_lr=1e-6,
            verbose=1,
        ),
    ]

    # 5. Train
    print(f"\n🚀 Training for up to {EPOCHS} epochs (early stopping enabled)...\n")
    model.fit(
        train_gen,
        validation_data=val_gen,
        epochs=EPOCHS,
        callbacks=callbacks,
    )

    # 6. Save labels (class index → folder name mapping)
    labels = list(train_gen.class_indices.keys())
    with open(LABELS_OUT, "w") as f:
        for label in labels:
            f.write(label + "\n")

    print(f"\n✅ Training complete!")
    print(f"   Model saved  : {MODEL_OUT}")
    print(f"   Labels saved : {LABELS_OUT} ({len(labels)} classes)")


if __name__ == "__main__":
    train()
