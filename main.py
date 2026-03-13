from server import Aggregator
from client import Client



# create an aggregator object
agg = Aggregator()

# save initial global weights
agg.save_global_weights()


# create a client object with the name : "client1"
client_1 = Client("client1")

# load the client1 model with the initial global weights
client_1.update_weights("./global_weights_iter/iter0.weights.h5")


# create a client object with the name : "client2"
client_2 = Client("client2")

# load the client1 model with the initial global weights
client_2.update_weights("./global_weights_iter/iter0.weights.h5")