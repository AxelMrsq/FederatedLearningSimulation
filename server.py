from model import global_model

import os
#https://docs.python.org/3/library/os.html



# aggregator class represent the server with the global model
class Aggregator:


    def __init__(self):
        print("")
        print("")
        print(f"Creating aggregator")
        #set up a global model and its initial weights
        self.model = global_model()

        #training iteration
        self.iter = 0


    # def get_global_weights(self): #return the global weights

    #     return self.model.get_weights()
    # get npy format of the model weights


    def save_global_weights(self): # save the global weights iteration
        
        # set the path of the weights iteration folder
        path = "./global_weights_iter"

        #https://docs.python.org/3/library/os.path.html#os.path.exists
        if os.path.exists(path) != True :

            #https://docs.python.org/3/library/os.html#os.makedirs
            os.makedirs(path)
        print("")
        print("")
        print(f"Saving weights of aggregator for the iteration {self.iter} in {path}")
        #https://www.tensorflow.org/api_docs/python/tf/keras/Model#save_weights
        self.model.save_weights(f"./global_weights_iter/iter{self.iter}.weights.h5")
        
        #update training iteration
        self.iter += 0


