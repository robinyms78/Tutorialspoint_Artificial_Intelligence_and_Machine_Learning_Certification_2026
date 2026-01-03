# import libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers 

# load the cifar dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

# preprocess the data
x_train = x_train.astype('float32')/255.0
x_test = x_test.astype('float32')/255.0

# define the model architecture
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation="softmax") 
])

# compiling the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# train the model
model.fit(x_train, y_train, batch_size=64, epochs=10, verbose=1)

# evaluate the model
loss, accuracy = model.evaluate(x_test, y_test, verbose=1)
print(f'test loss: {loss:.4f}')
print(f'test accuracy: {accuracy:.4f}')

# making prediction
predictions = model.predict(x_test[:5])
predicted_labels = tf.argmax(predictions, axis=1)
print(predicted_labels.numpy())

# https://keras.io/guides/