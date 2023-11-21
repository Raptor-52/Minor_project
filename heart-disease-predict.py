import streamlit as st
import pandas as pd
import numpy as np
import pickle

#loading the saved model
loaded_model=loaded_model = pickle.load(open('C:/Users/HP/Desktop/heart-disease/trained_model.sav', 'rb'))



st.write("""
# Heart disease Prediction App

This app predicts If a patient has a heart disease

Data obtained from Kaggle: https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset.
""")

st.sidebar.header('User Input Features')



# Collects user input features into dataframe
def heart_disease_predictor(input_data):
    input_data = (57,0,0,140,241,0,1,123,1,0.2,1,0,3)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
      return 'The person is not having heart disease'
    else:
      return 'The person is suffering from a heart disease'

def main():
      st.title("Heart Disease Prediction App")
    
      # Sidebar with user input
      st.sidebar.header("User Input Features")
    
      # Age
      age = st.sidebar.slider("Age", 18, 100, 25)
    
      # Sex
      sex = st.sidebar.radio("Sex", ["Female", "Male"])
    
      # Chest Pain Type
      cp = st.sidebar.selectbox("Chest Pain Type",
                                ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    
      # Resting Blood Pressure
      tres = st.sidebar.slider("Resting Blood Pressure (mm Hg)", 90, 200, 120)
    
      # Serum Cholesterol
      chol = st.sidebar.slider("Serum Cholesterol (mg/dl)", 100, 400, 200)
    
      # Fasting Blood Sugar
      fbs = st.sidebar.radio("Fasting Blood Sugar > 120 mg/dl", ["False", "True"])
    
      # Resting Electrocardiographic Results
      restecg = st.sidebar.selectbox("Resting Electrocardiographic Results",
                                     ["Normal", "ST-T Wave Abnormality", "Possible or Definite Left Ventricular Hypertrophy"])
    
      # Maximum Heart Rate Achieved
      thalach = st.sidebar.slider("Maximum Heart Rate Achieved", 70, 220, 120)
    
      # Exercise Induced Angina
      exang = st.sidebar.radio("Exercise Induced Angina", ["No", "Yes"])
    
      # ST Depression Induced by Exercise Relative to Rest
      oldpeak = st.sidebar.slider("ST Depression Induced by Exercise Relative to Rest", 0.0, 6.0, 0.0)
    
      # Slope of the Peak Exercise ST Segment
      slope = st.sidebar.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flatsloping", "Downslopins"])
    
      # Number of Major Vessels Colored by Flourosopy
      ca = st.sidebar.slider("Number of Major Vessels Colored by Flourosopy", 0, 3, 0)
    
      # Thalium Stress Result
      thal = st.sidebar.selectbox("Thalium Stress Result", ["Normal", "Fixed Defect", "Reversible Defect"])
    
      # Convert categorical input to numerical values
      sex = 1 if sex == "Male" else 0
      fbs = 1 if fbs == "True" else 0
      exang = 1 if exang == "Yes" else 0
    
      # Convert categorical input to numerical values for Chest Pain Type
      cp_mapping = {"Typical Angina": 0, "Atypical Angina": 1, "Non-Anginal Pain": 2, "Asymptomatic": 3}
      cp = cp_mapping[cp]
    
      # Convert categorical input to numerical values for Resting Electrocardiographic Results
      restecg_mapping = {"Normal": 0, "ST-T Wave Abnormality": 1, "Possible or Definite Left Ventricular Hypertrophy": 2}
      restecg = restecg_mapping[restecg]
    
      # Convert categorical input to numerical values for Slope of the Peak Exercise ST Segment
      slope_mapping = {"Upsloping": 0, "Flatsloping": 1, "Downslopins": 2}
      slope = slope_mapping[slope]
    
      # Convert categorical input to numerical values for Thalium Stress Result
      thal_mapping = {"Normal": 1, "Fixed Defect": 6, "Reversible Defect": 7}
      thal = thal_mapping[thal]

      # code for Prediction
      diagnosis = ''
        
      # creating a button for Prediction
        
      if st.button('Heart-Disease Test Result'):
          diagnosis = heart_disease_predictor([age, sex, cp, tres, chol, fbs, restecg_mapping, thalach,exang,oldpeak,slope,ca,thal])
            
            
      st.success(diagnosis)

    
if __name__ == '__main__':
    main()
    