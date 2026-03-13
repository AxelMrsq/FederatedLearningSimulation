from model import global_model

class Client:
    def __init__(self):
        # set up a edge model archi 
        self.model = global_model()

    def update_weights(self, weights):
        # update the edge model weights with the global one
        # https://www.tensorflow.org/api_docs/python/tf/keras/Sequential#load_weights
        self.model.load_weights(weights)

    def get_edge_weights(self):
        #return the edge weights
        return self.model.get_weights()

    