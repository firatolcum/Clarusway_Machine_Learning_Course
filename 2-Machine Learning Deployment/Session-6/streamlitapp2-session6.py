from textwrap import fill
import streamlit as st
import pickle
import pandas as pd
import requests
import json
import datetime

# Raw Data
#datetime,season,holiday,workingday,weather,temp,atemp,humidity,windspeed,casual,registered,count


st.sidebar.title('Bike-rental Prediction')

html_temp = """
<div style="background-color:blue;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML Cloud App</h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)


sample_one = ['2012-12-19 17:00:00',4,0,1,1,16.4,20.455,50,26.0027]



season=     st.sidebar.selectbox('What is the season?', (1,2,3,4))
holiday=     st.sidebar.selectbox('Is it holiday?', (0,1))
workingday=     st.sidebar.selectbox('Is it workingday?', (0,1))
weather=        st.sidebar.selectbox('How is the weather?', (1,2,3,4))
temp=         st.sidebar.slider('What is the temp?',1, 41, step=1)
atemp=         st.sidebar.slider('What is the atemp?',1, 45, step=1)
humidity=         st.sidebar.slider('What is the humidity?',1, 100, step=5)
windspeed=         st.sidebar.slider('What is the windspeed?',1, 56, step=3)
#casual=         st.sidebar.slider('What is the casual?',0, 367, step=20)
#registered=         st.sidebar.slider('What is the registered?',1, 886, step=50)


date1=str(st.date_input("enter date",value=datetime.date(2012, 12, 19), min_value=datetime.date(2011, 1, 1),max_value=datetime.date(2012, 12, 19)))
date2=str(st.time_input("Time", datetime.datetime.now()))
#date1=str(st.date_input("Date",datetime.datetime.now()))

url = 'https://f9urxt70a5.execute-api.us-east-1.amazonaws.com/beta2'

 
    



sample_one = [
date1+" "+date2,
 season,
 holiday,
 workingday,
 weather,
 temp,
 atemp,
 humidity,
 windspeed]

# Single Observation
request = {
    "instances": [
        {
            "features": sample_one
        }
    ]
}

request

response = requests.post(url, data=json.dumps(request))
result = response.json()

if result['statusCode'] == 200:
    predictions = json.loads(result['body'])
    st.write('Predicted Count: ', predictions)
else:
    print('Error',result['statusCode'], result['body'])

