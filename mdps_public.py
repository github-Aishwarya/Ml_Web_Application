# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:14:37 2022

@author: Lenovo
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('Heart_Disease_model.sav', 'rb'))

Breast_cancer_model = pickle.load(open('Breast_Cancer_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System ',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Breast Cancer Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)


    
    
    
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

    
# Breast Cancer Prediction Page
if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction using ML')
    
    col1, col2, col3,col4, col5 = st.columns(5)
    
    with col1:
        diagnosis = st.text_input('diagnosis')
        
    with col2:
        radius_mean = st.text_input('radius_mean')
        
    with col3:
        texture_mean = st.text_input('texture_mean')
        
    with col4:
        perimeter_mean = st.text_input('perimeter_mean')
        
    with col5:
        area_mean = st.text_input('area_mean')
        
    with col1:
        smoothness_mean = st.text_input('smoothness_mean')
        
    with col2:
        compactness_mean = st.text_input('compactness_mean')
        
    with col3:
        concavity_mean = st.text_input('concavity_mean')
        
    with col4:
        concave_points_mean = st.text_input('concave_points_mean')
        
    with col5:
        symmetry_mean = st.text_input('symmetry_mean')
        
    with col1:
        fractal_dimension_mean = st.text_input('fractal_dimension_mean')
        
    with col2:
        radius_se = st.text_input('radius_se')
        
    with col3:
        texture_se = st.text_input('texture_se')
        
    with col4:
        perimeter_se = st.text_input('perimeter_se')
        
    with col5:
        area_se = st.text_input('tarea_se')
        
    with col1:
        smoothness_se = st.text_input('smoothness_se')
    with col2:
        compactness_se = st.text_input('compactness_se')
        
    with col3:
        concavity_se = st.text_input('concavity_se')
        
    with col4:
        concave_points_se = st.text_input('concave_points_se')
        
    with col5:
        symmetry_se = st.text_input('symmetry_se')
        
    with col1:
        fractal_dimension_se = st.text_input('fractal_dimension_se')
        
    with col2:
        radius_worst = st.text_input('radius_worst')
        
    with col3:
        texture_worst = st.text_input('texture_worst')
         
    with col4:
        perimeter_worst = st.text_input('perimeter_worst')
                                        
    with col5:
        area_worst = st.text_input('area_worst')
        
    with col1:
        smoothness_worst = st.text_input('smoothness_worst')
        
    with col2:
        compactness_worst = st.text_input('compactness_worst')
        
    with col3:
        concavity_worst = st.text_input('concavity_worst')
        
    with col4:
        concave_points_worst = st.text_input('concave_points_worst')
        
    with col5:
        symmetry_worst = st.text_input('symmetry_worst')
        
    with col1:
        fractal_dimension_worst = st.text_input('fractal_dimension_worst')
         
    
     
     
                                        
     
    # code for Prediction
    Breast_Cancer_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having Breast Cancer'
        else:
          heart_diagnosis = 'The person does not have Breast Cancer'
        
    st.success(Breast_Cancer_diagnosis)
        
    
    

    
    