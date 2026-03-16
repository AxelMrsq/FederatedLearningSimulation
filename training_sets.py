from tensorflow.keras.utils import image_dataset_from_directory
#https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image_dataset_from_directory

# training set 1 client 1
train_ds_client1_set1 = image_dataset_from_directory(
    "working_dataset/FL_split/client_1_split_sets/set_1_split/train",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)

# validating set 1 client 1
val_ds_client1_set1 = image_dataset_from_directory(
    "working_dataset/FL_split/client_1_split_sets/set_1_split/val",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)

# testing set 1 client 1
test_ds_client1_set1 = image_dataset_from_directory(
    "working_dataset/FL_split/client_1_split_sets/set_1_split/test",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)


# training set 2 client 1
train_ds_client1_set2 = image_dataset_from_directory(
    "working_dataset/FL_split/client_1_split_sets/set_2_split/train",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)

# validating set 2 client 1
val_ds_client1_set2 = image_dataset_from_directory(
    "working_dataset/FL_split/client_1_split_sets/set_2_split/val",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)

# testing set 2 client 1
test_ds_client1_set2 = image_dataset_from_directory(
    "working_dataset/FL_split/client_1_split_sets/set_2_split/test",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)


# training set 3 client 1
train_ds_client1_set3 = image_dataset_from_directory(
    "working_dataset/FL_split/client_1_split_sets/set_3_split/train",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)

# validating set 3 client 1
val_ds_client1_set3 = image_dataset_from_directory(
    "working_dataset/FL_split/client_1_split_sets/set_3_split/val",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)

# testing set 3 client 1
test_ds_client1_set3 = image_dataset_from_directory(
    "working_dataset/FL_split/client_1_split_sets/set_3_split/test",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)


# training set 1 client 2
train_ds_client2_set1 = image_dataset_from_directory(
    "working_dataset/FL_split/client_2_split_sets/set_1_split/train",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)

# validating set 1 client 2
val_ds_client2_set1 = image_dataset_from_directory(
    "working_dataset/FL_split/client_2_split_sets/set_1_split/val",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)

# testing set 1 client 2
test_ds_client2_set1 = image_dataset_from_directory(
    "working_dataset/FL_split/client_2_split_sets/set_1_split/test",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)


# training set 2 client 2
train_ds_client2_set2 = image_dataset_from_directory(
    "working_dataset/FL_split/client_2_split_sets/set_2_split/train",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)

# validating set 2 client 2
val_ds_client2_set2 = image_dataset_from_directory(
    "working_dataset/FL_split/client_2_split_sets/set_2_split/val",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)

# testing set 2 client 2
test_ds_client2_set2 = image_dataset_from_directory(
    "working_dataset/FL_split/client_2_split_sets/set_2_split/test",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)


# training set 3 client 2
train_ds_client2_set3 = image_dataset_from_directory(
    "working_dataset/FL_split/client_2_split_sets/set_3_split/train",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)

# validating set 3 client 2
val_ds_client2_set3 = image_dataset_from_directory(
    "working_dataset/FL_split/client_2_split_sets/set_3_split/val",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)

# testing set 3 client 2
test_ds_client2_set3 = image_dataset_from_directory(
    "working_dataset/FL_split/client_2_split_sets/set_3_split/test",
    labels='inferred', #guess with the directories names
    label_mode='categorical', #categorical_crossentropy loss
    image_size=(64, 64),
    batch_size=32
)