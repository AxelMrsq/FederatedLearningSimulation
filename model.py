import tensorflow
#https://www.tensorflow.org/api_docs/python/tf

from tensorflow.keras.models import Sequential
#https://www.tensorflow.org/api_docs/python/tf/keras/models

from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
#https://www.tensorflow.org/api_docs/python/tf/keras/layers



#Initiate the global model architecture and weights
def global_model():

    model = Sequential()
    #https://www.tensorflow.org/api_docs/python/tf/keras/Sequential
    

    model.add(Conv2D(filters=32, kernel_size=3, activation="relu", input_shape=(64, 64, 3), kernel_initializer='glorot_uniform'))
    #https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D

    model.add(Conv2D(filters=32, kernel_size=3, activation="relu", kernel_initializer='glorot_uniform'))

    model.add(MaxPooling2D(pool_size=(2, 2)))
    #https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D


    model.add(Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), activation="relu", kernel_initializer="glorot_uniform",))

    model.add(Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), activation="relu", kernel_initializer="glorot_uniform",))

    model.add(MaxPooling2D(pool_size=(2, 2)))


    model.add(Flatten()) 

    #https://www.tensorflow.org/api_docs/python/tf/keras/layers/Flatten
    model.add(Dense(units=512, activation="relu", kernel_initializer='glorot_uniform')) 

    #https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense
    model.add(Dense(units=5, activation="softmax", kernel_initializer='glorot_uniform')) 
    
    #return the model architecture object
    return model
