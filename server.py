from model import global_model

class Aggregator:
    def __init__(self):
        #set up a global model and its initial weights
        self.model = global_model()

    def get_global_weights(self):
        #return the global weights
        return self.model.get_weights()

    def save_global_weights(self):
        # save the global weights
        #https://www.tensorflow.org/api_docs/python/tf/keras/Model#save_weights
        self.model.save_weights("data.weights.h5")
