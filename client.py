from model import global_model

import os 
#https://docs.python.org/3/library/os.html



#client class to represent an edge nodewith a local model
class Client:


    def __init__(self, name): #initiate a client

        # set up a edge model archi 
        self.model = global_model()

        # client name
        self.name = name
        
        # training iteration
        self.iter = 0


    def update_weights(self, weights): # update the edge model weights with the global one

        # https://www.tensorflow.org/api_docs/python/tf/keras/Sequential#load_weights
        self.model.load_weights(weights)
        # Replace the weights of the local model


    # def get_edge_weights(self): #return the edge weights

    #     return self.model.get_weights() 
    # get npy format of the model weights


    def save_edge_weights(self) : # save the edge weights iteration

        # set the path of the weights iteration folder
        path = f"./{self.name}_weights_iter"
        
        #https://docs.python.org/3/library/os.path.html#os.path.exists
        if os.path.exist != True :
            
            #https://docs.python.org/3/library/os.html#os.makedirs
            os.makedirs(path)

        #https://www.tensorflow.org/api_docs/python/tf/keras/Model#save_weights
        self.model.save_weights(f"./{self.name}_weights_iter/iter{self.iter}.weights.h5")

        #update iteration
        self.iter += 1

    