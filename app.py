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
    "Age": [age],
    "Sex": [sex],
    "BP": [bp],
    "Cholesterol": [chol],
    "Na_to_K": [na_to_k]
})

if st.button("Predict"):
    prediction = model.predict(data)
    st.success(f"Predicted Drug Type: {prediction[0]}")