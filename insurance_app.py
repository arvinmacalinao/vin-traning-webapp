import streamlit as st
import numpy as np
import pandas as pd
import joblib
import time

st.title("Insurance Pricing App")
st.write("From the insurance data, we built a machine learning model for pricing insurance claims.")

st.sidebar.title("")
st.sidebar.write("")

#Age
age = st.sidebar.slider("Age", 0, 100, 24)

#Age

bmi = st.sidebar.slider("BMI", 15, 40, 29)

#Number of childer
num_children = st.sidebar.slider("Number of Children", 0, 12, 1)

#Gender
gender = st.sidebar.radio("Gender", ('femail', 'male'))

if gender == 'male':
    is_female = 0
else:
    is_female = 1
    
# Is Smoker
smoker = st.sidebar.radio("Smoker?" , ('yes', 'no'))

if smoker == 'yes':
    is_smoker = 1
else:
    is_smoker = 0
    
# Region
region = st.sidebar.selectbox("Region", ['northwest', 'northeast', 'southeast', 'southwest'])

if region == 'northeast':
    loc_list = [1, 0, 0, 0]
elif region == 'northwest':
    loc_list = [0, 1, 0, 0]
elif region == 'southeast':
    loc_list = [0, 0, 1, 0]
elif region == 'southwest':
    loc_list = [0, 0, 0, 1]

### Price Output
st.subheader('Output Insurance Price')

# Model filename
filename = 'finalized_model.sav'

# Load the model from disk
loaded_model = joblib.load(filename)

# 
prediction = round(loaded_model.predict([[age, bmi, num_children, is_female, is_smoker] + loc_list])[0])

st.write(f"Suggested Insurance Price is: {prediction}")

    