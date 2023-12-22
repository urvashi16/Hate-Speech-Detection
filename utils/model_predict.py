import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

model_dir = "models/"
FILEPATH_MAPPER = {"T": "traditional_model.h5", "L": "lstm_model.h5", "F": "fusion_model.h5"}
def predict(text, model_code = "T"):
    model_path = os.path.join(model_dir, FILEPATH_MAPPER[model_code])


    # Load the model
    encoding = preprocess_text(text, model_code)
    if model_code == "L":
        model = tf.keras.models.load_model(model_path)

    elif model_code == "T":
        model = pickle.load(open(model_path, "rb"))
    
    
    y_pred = (model.predict(encoding) > 0.5).astype(int)

    if model_code == "L":
        return y_pred[0, 0]
    
    elif model_code == "T":
        return y_pred[0]

    # Make the prediction 

    # Return the prediction


    return None


def preprocess_text(text, model_code = "T"):

    if model_code == "L" or model_code == "T":
 
        token = pickle.load(open("utils/token.pkl", "rb"))

        encoding = pad_sequences(token.texts_to_sequences(np.array([text])), maxlen = 50)

        return encoding

    elif model_code == "F":
        pass