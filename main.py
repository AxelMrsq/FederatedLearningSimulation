from server import Aggregator
from client import Client


import numpy 

#verify if two identic models have the same weights
def compare_keras_models(model_1, model_2):
    weights_1 = model_1.get_weights()
    weights_2 = model_2.get_weights()

    if len(weights_1) != len(weights_2):
        return False

    for w1, w2 in zip(weights_1, weights_2):
        # np.array_equal vérifie si la forme et les valeurs sont identiques
        if not numpy.array_equal(w1, w2):
            return False
            
    return True

agg = Aggregator()
agg.save_global_weights()


client_1 = Client()
client_1.update_weights("data.weights.h5")

print(compare_keras_models(agg.model, client_1.model))
