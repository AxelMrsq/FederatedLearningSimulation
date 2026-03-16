from server import Aggregator

from client import Client

from training_sets import train_ds_client1_set1, train_ds_client1_set2, train_ds_client1_set3, val_ds_client1_set1, val_ds_client1_set2, val_ds_client1_set3, test_ds_client1_set1, test_ds_client1_set2, test_ds_client1_set3, train_ds_client2_set1, train_ds_client2_set2, train_ds_client2_set3, val_ds_client2_set1, val_ds_client2_set2, val_ds_client2_set3, test_ds_client2_set1, test_ds_client2_set2, test_ds_client2_set3

# create a client object with the name : "client1"
client_1 = Client("client1")

# create a client object with the name : "client2"
client_2 = Client("client2")

# create an aggregator object
agg = Aggregator()

# save initial global weights
agg.save_global_weights()


# load the client1 model with the initial global weights
client_1.update_weights("./global_weights_iter/iter0.weights.h5")

# load the client1 model with the initial global weights
client_2.update_weights("./global_weights_iter/iter0.weights.h5")


# first local iteration training on client 1
client_1.train_local_model(train_ds_client1_set1, val_ds_client1_set1)

# first local iteration training on client 2
client_2.train_local_model(train_ds_client2_set1, val_ds_client2_set1)

#https://www.tensorflow.org/api_docs/python/tf/keras/Layer#get_weights
agg.aggregate_weights(client_1.model.get_weights(), client_2.model.get_weights())


# save initial global weights
agg.save_global_weights()


# load the client1 model with the initial global weights
client_1.update_weights("./global_weights_iter/iter1.weights.h5")

# load the client1 model with the initial global weights
client_2.update_weights("./global_weights_iter/iter1.weights.h5")


# first local iteration training on client 1
client_1.train_local_model(train_ds_client1_set2, val_ds_client1_set2)

# first local iteration training on client 2
client_2.train_local_model(train_ds_client2_set2, val_ds_client2_set2)
