import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write(
    """
    # Simple Iris Flower Prediction App

    This application predicts the Iris flower type!
    """
)

st.sidebar.header("User Input Parameters")

def user_input_features():
    sepal_length = st.sidebar.slider("sepal_length", 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider("sepal width", 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider("petal_length", 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider("petal_width", 0.1, 2.5, 0.2)
    data = {"sepal_length" : sepal_length,
            "sepal_width" : sepal_width,
            "petal_length" : petal_length,
            "petal_width" : petal_width}
    features = pd.DataFrame(data, index = [0])
    return features

df = user_input_features()

st.subheader("User Input Parameters")
st.write("**Sepal Length:**",df["sepal_length"][0],
         "**Sepal Width:**", df["sepal_width"][0],
         "**Petal Length:**", df["petal_length"][0],
         "**Petal Width:**", df["petal_width"][0])

iris = datasets.load_iris()
X = iris.data
y = iris.target

rf_model = RandomForestClassifier()
rf_model.fit(X, y)

prediction = rf_model.predict(df)
prediction_proba = rf_model.predict_proba(df)

st.subheader("Class labels and their corresponding index number")
st.write(iris.target_names)

st.subheader("Prediction")
st.write("Model Prediction is :", iris.target_names[prediction[0]])
st.write("Class number is :", prediction[0])
st.write("Prediction probability is:", prediction_proba)