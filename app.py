import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Drug Response Prediction")

age = st.number_input("Age")
na = st.number_input("Na")
k = st.number_input("K")

sex = st.selectbox("Sex", ["M", "F"])
bp = st.selectbox("BP", ["LOW", "NORMAL", "HIGH"])
chol = st.selectbox("Cholesterol", ["NORMAL", "HIGH"])

if st.button("Predict"):

    # Step 1: Normal dataframe create pannunga
    data = pd.DataFrame({
        "Age": [age],
        "Na": [na],
        "K": [k],
        "Sex": [sex],
        "BP": [bp],
        "Cholesterol": [chol]
    })

    # 🔥 Step 2: Insert here
    data = pd.get_dummies(data)

    # 🔥 Step 3: Insert here
    data = data.reindex(columns=model.feature_names_in_, fill_value=0)

    # Step 4: Prediction
    prediction = model.predict(data)

    st.success(f"Predicted Drug: {prediction[0]}")