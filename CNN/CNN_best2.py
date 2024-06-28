import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
import json
import keras
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
from tensorflow.keras.regularizers import l2
import pickle

train_ds = keras.utils.image_dataset_from_directory(
    # directory='/Volumes/PRO-G40/Scriptie/data/training_data',
    directory='/home/tsplint/thesis/data/data256+/training_data',
    labels='inferred',
    label_mode='binary',
    batch_size=128,
    image_size=(256, 256)
)
validation_ds = keras.utils.image_dataset_from_directory(
    # directory='/Volumes/PRO-G40/Scriptie/data/testing_data',
    directory='/home/tsplint/thesis/data/data256+/testing_data',
    labels='inferred',
    label_mode='binary',
    batch_size=128,
    image_size=(256, 256)
)

callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=100, restore_best_weights=True)

inputShape = (256, 256, 3)

model = Sequential([
    Conv2D(16, (3, 3), activation='relu', padding='same', input_shape=inputShape, kernel_regularizer=l2(0.001)),
    BatchNormalization(),
    MaxPooling2D((2, 2)),

    Conv2D(32, (3, 3), activation='relu', padding='same', kernel_regularizer=l2(0.001)),
    BatchNormalization(),
    MaxPooling2D((2, 2)),

    Conv2D(32, (3, 3), activation='relu', padding='same', kernel_regularizer=l2(0.001)),
    BatchNormalization(),
    MaxPooling2D((2, 2)),

    Conv2D(64, (3, 3), activation='relu', padding='same', kernel_regularizer=l2(0.001)),
    BatchNormalization(),
    MaxPooling2D((2, 2)),

    Conv2D(64, (3, 3), activation='relu', padding='same', kernel_regularizer=l2(0.001)),
    BatchNormalization(),
    MaxPooling2D((2, 2)),

    Conv2D(128, (3, 3), activation='relu', padding='same', kernel_regularizer=l2(0.001)),
    BatchNormalization(),
    MaxPooling2D((2, 2)),

    Conv2D(128, (3, 3), activation='relu', padding='same', kernel_regularizer=l2(0.001)),
    BatchNormalization(),
    MaxPooling2D((2, 2)),

    Conv2D(256, (3, 3), activation='relu', padding='same', kernel_regularizer=l2(0.001)),
    BatchNormalization(),
    MaxPooling2D((2, 2)),

    Flatten(),
    Dense(256, activation='relu', kernel_regularizer=l2(0.001)),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

print("Number of parameters: ", model.count_params())

# Compile the model
model.compile(optimizer='adam',
                loss='binary_crossentropy',
                metrics=['accuracy'])

# Train the model
history = model.fit(train_ds, validation_data=validation_ds, epochs=2000, callbacks=[callback])

# Save the model
model.save('CNN/best_model2/CNN_best2.h5')

# Plot training and validation accuracy
plt.figure(figsize=(10, 6))
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.grid(True)
plt.savefig('CNN/best_model2/CNN_best2_accuracy.png')
plt.show()

# Plot training and validation loss
plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(loc='upper right')
plt.grid(True)
plt.savefig('CNN/best_model2/CNN_best2_loss.png')
plt.show()

# Evaluate the model
loss, accuracy = model.evaluate(validation_ds)
print("Accuracy: ", accuracy)
print("Loss: ", loss)

# Save the training history
with open('CNN/best_model2/history.pkl', 'wb') as f:
    pickle.dump(history.history, f)

