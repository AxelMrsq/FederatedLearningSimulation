import tensorflow
from tensorflow.keras.utils import image_dataset_from_directory

train_ds = image_dataset_from_directory(
    "./working_dataset/split/train",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)

val_ds = image_dataset_from_directory(
    "./working_dataset/split/val",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)

test_ds = image_dataset_from_directory(
    "./working_dataset/split/test",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

def Baseline_CNN_architecture_vgglite() :
     model = Sequential()

     # Input shape should be (height, width, channels) for TensorFlow backend
     model.add(Conv2D(filters=32, kernel_size=(3, 3), strides=(1, 1), input_shape=(64, 64, 3), activation="relu", kernel_initializer="glorot_uniform",))
     model.add(Conv2D(filters=32, kernel_size=(3, 3), strides=(1, 1), activation="relu", kernel_initializer="glorot_uniform",))

     model.add(MaxPooling2D(pool_size=(2, 2)))

     model.add(Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), activation="relu", kernel_initializer="glorot_uniform",))
     model.add(Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), activation="relu", kernel_initializer="glorot_uniform",))

     model.add(MaxPooling2D(pool_size=(2, 2)))

     model.add(Flatten()) # Corrected: Removed duplicate model.add
     model.add(Dense(units=512, activation="relu")) # Added activation for hidden layer
     model.add(Dense(units=5, activation="softmax")) # Use num_classes for output units
     return model

from tensorflow.keras.optimizers import SGD

sgd = SGD(learning_rate=0.001)

model = Baseline_CNN_architecture_vgglite()
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

history = model.fit(train_ds, validation_data=val_ds, epochs=10)