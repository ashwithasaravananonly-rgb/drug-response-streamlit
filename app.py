import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Drug Response Prediction")

# Input fields
age = st.number_input("Age")
na = st.number_input("Na")
k = st.number_input("K")

sex = st.selectbox("Sex", ["M", "F"])
bp = st.selectbox("BP", ["LOW", "NORMAL", "HIGH"])
chol = st.selectbox("Cholesterol", ["NORMAL", "HIGH"])

if st.button("Predict"):

    data = pd.DataFrame({
        'Age': [age],
        'Na': [na],
        'K': [k],
        'Sex_F': [1 if sex == "F" else 0],
        'Sex_M': [1 if sex == "M" else 0],
        'BP_HIGH': [1 if bp == "HIGH" else 0],
        'BP_LOW': [1 if bp == "LOW" else 0],
        'BP_NORMAL': [1 if bp == "NORMAL" else 0],
        'Cholesterol_HIGH': [1 if chol == "HIGH" else 0],
        'Cholesterol_NORMAL': [1 if chol == "NORMAL" else 0]
    })

    prediction = model.predict(data)

    st.success(f"Predicted Drug: {prediction[0]}")