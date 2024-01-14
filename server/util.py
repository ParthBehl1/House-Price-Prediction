import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bath,bhk):
    try:
        location_index = __data_columns.index(location.lower())
    except:
        location_index=-1
    features = np.zeros(len(__data_columns))
    features[0] = sqft
    features[1] = bath
    features[2] = bhk
    if location_index >= 0:
        features[location_index] = 1
    return round(__model.predict([features])[0],2)
def get_locations():
    return __locations

def load_saved_artifacts():
    print("loading..")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[3:]


    global __model
    with open("./artifacts/house_prediction_prices.pickle", 'rb') as f:
        __model=pickle.load(f)
    print("loading done")


if __name__ =="__main__":
    load_saved_artifacts()
    print(get_locations())
    print(get_estimated_price('1st Phase JP Nagar',1000,2,3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))