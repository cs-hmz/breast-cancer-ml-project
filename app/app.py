import streamlit as st
import requests

st.title("Breast Cancer Prediction App")

features = []
for i in range(30):  # number of features
    val = st.number_input(f"Feature {i+1}", value=0.0)
    features.append(val)

if st.button("Predict"):
    response = requests.post("http://127.0.0.1:8000/predict", json={"features": features})
    result = response.json()["diagnosis"]
    if result == 1:
        st.error("⚠️ Malignant Tumor")
    else:
        st.success("✅ Benign Tumor")
