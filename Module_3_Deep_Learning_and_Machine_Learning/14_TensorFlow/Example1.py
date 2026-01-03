# importing libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# loading the data
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# preprocessing the data
x_train = x_train.reshape(-1, 28*28).astype("float32")/255.0
x_test = x_test.reshape(-1, 28*28).astype("float32")/255.0

# model architecture
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(28*28,)),
    layers.Dense(64, activation='relu'), 
    layers.Dense(10, activation='softmax')
])

# compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# train the model
model.fit(x_train, y_train, batch_size=32, epochs=5, verbose=1)

# evaluate the model
loss, accuracy = model.evaluate(x_test, y_test, verbose=1)
print(f'test loss:{loss:.4f}')
print(f'test accuracy:{accuracy:.4f}')

# make predictions
pred = model.predict(x_test[:5])
pred_labels=tf.argmax(pred, axis=1)

# print predictions
print(pred_labels.numpy())

# https://www.tensorflow.org/api_docs/python/tf