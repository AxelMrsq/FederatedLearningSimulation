from model import global_model

import os 
#https://docs.python.org/3/library/os.html

from tensorflow.keras.optimizers import SGD
#https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/SGD



#client class to represent an edge nodewith a local model
class Client:


    def __init__(self, name): #initiate a client
        
        
        # set up a edge model archi 
        self.model = global_model()

        # set up a edge optimizer
        self.sgd = SGD(learning_rate=0.001)

        # client name
        self.name = name
        
        # training iteration
        self.iter = 0
        print("")
        print("")
        print(f"Creating {self.name}")


    def update_weights(self, weights): # update the edge model weights with the global one
        
        print("")
        print("")
        print(f"Loading weights on the model of {self.name}")
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
        if os.path.exists(path) != True :
            
            #https://docs.python.org/3/library/os.html#os.makedirs
            os.makedirs(path)
         
        print("")
        print("")
        print(f"Saving weights of model of {self.name} for iteration {self.iter} in {path}")
        #https://www.tensorflow.org/api_docs/python/tf/keras/Model#save_weights
        self.model.save_weights(f"./{self.name}_weights_iter/iter{self.iter}.weights.h5")

        #update iteration
        self.iter += 1

    
    def train_local_model(self, train_ds, val_ds, epochs=2):
        
        print("")
        print("")
        print(f"Compiling model of {self.name}")
        #compile the local model and the local optimizer
        #https://www.tensorflow.org/api_docs/python/tf/keras/Model#compile
        self.model.compile(loss='categorical_crossentropy', optimizer=self.sgd, metrics=['accuracy'])
        
        print("")
        print("")
        print(f"Fitting model of {self.name}")
        # train the model with X epochs
        #https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit
        self.model.fit(train_ds, validation_data=val_ds, epochs=epochs)
        
        # save new local parameters
        self.save_edge_weights()