import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow info/warning messages

import tensorflow as tf
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from sklearn.model_selection import train_test_split

# Load the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Preprocess the images
X_train = X_train / 255.0
X_test = X_test / 255.0

# Split the dataset into training, validation, and test sets
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Define the neural network architecture
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Flatten the 28x28 input images into a 1D array
    Dense(128, activation='relu'),    # First dense layer with 128 units and ReLU activation
    Dense(10, activation='softmax')   # Output layer with 10 units for 10 classes (digits 0 to 9) and softmax activation
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=5, batchsize = 32, validation_data=(X_val, y_val))

# Evaluate the model on the test set and print the loss and accuracy
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")
