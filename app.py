import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Load training columns
columns = pickle.load(open("columns.pkl", "rb"))

st.title("Drug Response Prediction")

age = st.number_input("Age")
na = st.number_input("Na")
k = st.number_input("K")

sex = st.selectbox("Sex", ["M", "F"])
bp = st.selectbox("BP", ["LOW", "NORMAL", "HIGH"]])
chol = st.selectbox("Cholesterol", ["NORMAL", "HIGH"])

if st.button("Predict"):

    data = pd.DataFrame({
        "Age": [age],
        "Na": [na],
        "K": [k],
        "Sex": [sex],
        "BP": [bp],
        "Cholesterol": [chol]
    })

    # Convert like training
    data = pd.get_dummies(data)

    # Match training columns
    data = data.reindex(columns=columns, fill_value=0)

    prediction = model.predict(data)

    st.success(f"Predicted Drug: {prediction[0]}")