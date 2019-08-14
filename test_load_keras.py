import keras
from keras.models import Sequential, Model
from keras.layers import InputLayer, Input
from keras.layers import Reshape, MaxPooling2D, AveragePooling2D, concatenate
from tensorflow.python.keras.layers import Conv2D, Dense, Flatten
from keras.models import load_model

model = load_model('E:\\MachineLearningModels\\keras\\new_model.h5')
model.summary()
for weight in model.weights:
    print(weight)