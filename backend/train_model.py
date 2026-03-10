import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
import os

# Paths
base_dir = '/Users/omkarpanchal/Downloads/CHK-1772702884642-6141-main/CHK-1772702884642-6141-main/backend/archive-2/New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)'
train_dir = os.path.join(base_dir, 'train')
valid_dir = os.path.join(base_dir, 'valid')

# Image parameters
img_height = 224
img_width = 224
batch_size = 32

# Data Generators
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

valid_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'
)

valid_generator = valid_datagen.flow_from_directory(
    valid_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'
)

# Number of classes
num_classes = train_generator.num_classes
print(f"Number of classes: {num_classes}")

# Build Model (using MobileNetV2 for faster training and good accuracy)
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(img_height, img_width, 3))
base_model.trainable = False # Freeze base model layers initially

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train Model
print("Starting training...")
epochs = 5 # Starting with a small number of epochs for demonstration. Can be increased later.
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    validation_data=valid_generator,
    validation_steps=valid_generator.samples // batch_size,
    epochs=epochs
)

# Save Model
model.save('crop_disease_model_new.h5')
print("Model saved to crop_disease_model_new.h5")

# Save class labels
class_indices = train_generator.class_indices
labels = list(class_indices.keys())
with open('labels_new.txt', 'w') as f:
    for label in labels:
        f.write(f"{label}\n")
print("Labels saved to labels_new.txt")

