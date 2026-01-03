# importing libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers 

# loading the data
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# preprocessing the data
x_train = x_train.reshape(-1, 28*28).astype("float32")/255.0
x_test = x_test.reshape(-1, 28*28).astype("float32")/255.0

# defining the model architecture
model = tf.keras.Sequential([
    layers.SimpleRNN(64, input_shape=(28, 28)),
    layers.Dense(10, activation='softmax')
])

# compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# reshaping the input data
x_train = x_train.reshape((-1, 28, 28))

# train the model
model.fit(x_train, y_train, batch_size=32, epochs=5, verbose=1)

# reshaping the input data
x_test = x_test.reshape((-1, 28,28))

# evaluate the model
loss, accuracy = model.evaluate(x_test, y_test, verbose=1)
print(f'test loss: {loss:.4f}')
print(f'test accuracy: {accuracy:.4f}')

