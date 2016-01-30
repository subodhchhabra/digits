""";x

"""
import csv
import json
import os
import pandas as pd
import pickle
import numpy as np

def get_paths():
    paths = json.loads(open("SETTINGS.json").read())
    for key in paths:
        paths[key] = os.path.expandvars(paths[key])
    return paths

def identity(x):
    return x

def get_train_df():
    train_path = get_paths()["train_data_path"]
    return pd.read_csv(train_path)

def get_valid_df():
    valid_path = get_paths()["valid_data_path"]
    return pd.read_csv(valid_path)

def save_model(model):
    out_path = get_paths()["model_path"]
    pickle.dump(model, open(out_path, "wb"))

def load_model():
    in_path = get_paths()["model_path"]
    return pickle.load(open(in_path, "rb"))

def write_submission(predictions):
    prediction_path = get_paths()["prediction_path"]
    
    writer = csv.writer(open(prediction_path, "w"), lineterminator="\n")
    valid = get_valid_df()
    rows = [x for x in zip(valid.index + 1, predictions.flatten().astype(int))] # id starts at 1 not 0.
    writer.writerow(("ImageId", "Label"))
    writer.writerows(rows)
    """
    print('saving predictions to {path}'.format(path=prediction_path))
    np.savetxt(prediction_path, predictions, delimiter=',') 
    print('prediction saved.')
    """
