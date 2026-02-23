import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Drug Response Prediction")

# Input fields
age = st.number_input("Age")
sex = st.selectbox("Sex", ["M", "F"])
bp = st.selectbox("BP", ["LOW", "NORMAL", "HIGH"])
chol = st.selectbox("Cholesterol", ["NORMAL", "HIGH"])
na_to_k = st.number_input("Na_to_K")

# Convert to dataframe
data = pd.DataFrame({
data = pd.DataFrame([[ 
    age,
    na_to_k,
    1 if sex=="F" else 0,
    1 if sex=="M" else 0,
    1 if bp=="HIGH" else 0,
    1 if bp=="LOW" else 0,
    1 if bp=="NORMAL" else 0,
    1 if chol=="HIGH" else 0,
    1 if chol=="NORMAL" else 0
]], columns=[
    'Age',
    'Na_to_K',
    'Sex_F',
    'Sex_M',
    'BP_HIGH',
    'BP_LOW',
    'BP_NORMAL',
    'Cholesterol_HIGH',
    'Cholesterol_NORMAL'
])})
# Encoding (IMPORTANT)
data['Sex'] = data['Sex'].map({'F':0, 'M':1})
data['BP'] = data['BP'].map({'LOW':0,'NORMAL':1,'HIGH':2})
data['Cholesterol'] = data['Cholesterol'].map({'NORMAL':0,'HIGH':1})

if st.button("Predict"):
    prediction = model.predict(data)
    st.success(f"Predicted Drug Type: {prediction[0]}")