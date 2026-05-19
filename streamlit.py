import streamlit as st
import requests

st.title("Iris Prediction App")

st.write("Enter 4 feature values from Iris dataset")

feature1 = st.number_input("Sepal Length")
feature2 = st.number_input("Sepal Width")
feature3 = st.number_input("Petal Length")
feature4 = st.number_input("Petal Width")

if st.button("Predict"):

    input_data = {
        "features": [
            feature1,
            feature2,
            feature3,
            feature4
        ]
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=input_data
    )

    prediction = response.json()["prediction"]

    species = {
        0: "Setosa",
        1: "Versicolor",
        2: "Virginica"
    }

    st.success(f"Prediction: {species[prediction]}")