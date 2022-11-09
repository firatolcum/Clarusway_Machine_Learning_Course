from email.mime import image
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

scaler_iris = pickle.load(open("scaler_iris.pickle", "rb"))
final_model = pickle.load(open("final_model_iris.pickle", "rb"))


html_temp = """
<div style="background-color:purple;padding:1.5px">
<h1 style="color:white;text-align:center;">Select Flower Features</h1>
</div><br>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)

html_temp2 = """
<div style="background-color:purple;padding:1.5px">
<h1 style="color:white;text-align:center;">Flower Type Prediction App</h1>
</div><br>"""
st.markdown(html_temp2,unsafe_allow_html=True)

img = Image.open("iris.png")
st.image(img, use_column_width=True)

st.info("**Click the arrow in the upper left\
    corner to open the sidebar and select features of the flower.**")



sepal_length_cm = st.sidebar.number_input("Sepal Length (cm)",4.3, 7.9)
sepal_width_cm = st.sidebar.number_input("Sepal Width (cm)", 2.0, 4.4)
petal_length_cm = st.sidebar.number_input("Petal Length (cm)", 1.0, 6.9)
petal_width_cm = st.sidebar.number_input("Petal Width (cm)", 0.1, 2.5)

new_data = {    "sepal_length_cm" : sepal_length_cm,
                "sepal_width_cm" : sepal_width_cm,
                "petal_length_cm" : petal_length_cm,
                "petal_width_cm" : petal_width_cm

            }
new_data_df = pd.DataFrame([new_data])

new_data_scale = scaler_iris.transform(new_data_df)
prediction = final_model.predict(new_data_scale)

prediction_proba = final_model.predict_proba(new_data_scale)
setosa_proba = prediction_proba[:,0]
versicolor_proba = prediction_proba[:,1]
virginica_proba = prediction_proba[:,2]

st.write(new_data_df)
st.info("**Check the features you selected from the table above. If correct, press the Predict button.**")

if st.button("Make Predict"):
    if prediction[0] == "Iris-setosa":
        st.success(f"There is a **{round(setosa_proba[0] * 100, 1)}%** probability that your flower type is **{prediction[0]}**")
    elif prediction[0] == "Iris-versicolor":
        st.success(f"There is a **{round(versicolor_proba[0] * 100, 1)}%** probability that your flower type is **{prediction[0]}**")
    elif prediction[0] == "Iris-virginica" :
        st.success(f"There is a **{round(virginica_proba[0] * 100, 1)}%** probability that your flower type is **{prediction[0]}**")
    