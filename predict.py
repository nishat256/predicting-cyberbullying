import pickle
import numpy as np
from keras.models import load_model
from tensorflow.keras import backend 
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# loading tokenizer
with open('model/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
# loading model
model = load_model('model/model_weights.hdf5')

def predict_output(input_text):
    sequence = tokenizer.texts_to_sequences([input_text])
    padded_sequence = pad_sequences(sequence,maxlen=100)
    prediction = model.predict(padded_sequence)
    resp =  process_prediction(prediction)
    return resp

def process_prediction(input_array):
    indices = np.nonzero(input_array[0] > .5)
    labels = ['toxic','severe_toxic','obscene','threat','insult','identity_hate']
    output_labels = []
    for index in indices[0]:
        output_labels.append(labels[index])
    return output_labels


if __name__ == "__main__":
    input_text = "you are looking very fat ugly like a cow"
    print(predict_output(input_text))