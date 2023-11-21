# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle


loaded_model = pickle.load(open('C:/Users/HP/Desktop/heart-disease/trained_model.sav', 'rb'))

input_data = (57,0,0,140,241,0,1,123,1,0.2,1,0,3)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not having heart disease')
else:
  print('The person is suffering from a heart disease')