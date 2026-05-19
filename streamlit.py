import streamlit as st
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("Iris Flower Prediction")

st.write("Enter flower measurements")

feature1 = st.number_input("Sepal Length")
feature2 = st.number_input("Sepal Width")
feature3 = st.number_input("Petal Length")
feature4 = st.number_input("Petal Width")

if st.button("Predict"):

    features = [[
        feature1,
        feature2,
        feature3,
        feature4
    ]]

    prediction = model.predict(features)

    species = {
        0: "Setosa",
        1: "Versicolor",
        2: "Virginica"
    }

    st.success(f"Prediction: {species[prediction[0]]}")