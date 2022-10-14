from textwrap import fill
import streamlit as st
import pickle
import pandas as pd
import requests
import json
import datetime

# Raw Data
#datetime,season,holiday,workingday,weather,temp,atemp,humidity,windspeed,casual,registered,count
# Actual=562

st.sidebar.title('Cancer Prediction')

html_temp = """
<div style="background-color:blue;padding:10px">
<h2 style="color:white;text-align:center;">Invoke Sagemaker via Steramlit</h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)



radius_mean=st.sidebar.slider('What is the radius_mean?',6.981000, 28.110000, step=1.1)
texture_mean=20.38
perimeter_mean=122.8
area_mean=1001.0
smoothness_mean=0.1184
compactness_mean=0.2776
concavity_mean=0.3001
concave_points_mean=0.1471
symmetry_mean=0.2419
fractal_dimension_mean=0.07871
radius_se=1.095
texture_se=0.9053
perimeter_se=8.589
area_se=153.4
smoothness_se=0.006399
compactness_se=0.04904
concavity_se=0.05372999999999999
concave_points_se=0.01587
symmetry_se=0.03003
fractal_dimension_se=0.006193
radius_worst=25.38
texture_worst=17.33
perimeter_worst=184.6
area_worst=2019.0
smoothness_worst=0.1622
compactness_worst=0.6656
concavity_worst=0.7119
concave_points_worst=0.2654
symmetry_worst=0.4601
fractal_dimension_worst=0.1189






url = 'https://84n4udr65l.execute-api.us-east-1.amazonaws.com/beta2'

 
    


# Raw Data
#datetime,season,holiday,workingday,weather,temp,atemp,humidity,windspeed,casual,registered,count
# Actual=562
sample_one = [
       radius_mean,
    texture_mean,
    perimeter_mean,
    area_mean,
    smoothness_mean,
    compactness_mean,
    concavity_mean,
    concave_points_mean,
    symmetry_mean,
    fractal_dimension_mean,
    radius_se,
    texture_se,
    perimeter_se,
    area_se,
    smoothness_se,
    compactness_se,
    concavity_se,
    concave_points_se,
    symmetry_se,
    fractal_dimension_se,
    radius_worst,
    texture_worst,
    perimeter_worst,
    area_worst,
    smoothness_worst,
    compactness_worst,
    concavity_worst,
    concave_points_worst,
    symmetry_worst,
    fractal_dimension_worst,
]
sample_two={"data":"13.49,22.3,86.91,561.0,0.08752,0.07697999999999999,0.047510000000000004,0.033839999999999995,0.1809,0.057179999999999995,0.2338,1.3530000000000002,1.735,20.2,0.004455,0.013819999999999999,0.02095,0.01184,0.01641,0.001956,15.15,31.82,99.0,698.8,0.1162,0.1711,0.2282,0.1282,0.2871,0.06917000000000001"}

data={"data":str(sample_one).replace("[","").replace("]","")}

response = requests.post(url, json.dumps(data))
result = response.json()
st.write(result)










    
