
from fileinput import filename
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("This is a title")
st.text("This is some text")
st.markdown("Streamlit is **_really_ cool** :+1:")
st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.header("This is a header")
st.subheader("This is a subheader")

st.success("This is a success message!")
st.info("This is a purely informational message")
st.error("This is an error")

st.help(range)

st.write("Hello *World!* :sunglasses:")

#image
img = Image.open("images.jpeg")
st.image(img, caption="cattie", width=300)

#my_video = open("ml.mov", "rb")
st.video("https://www.youtube.com/watch?v=uHKfrz65KSU")

#Checkbox
cbox = st.checkbox("Hide and Seek")
if cbox:
    st.write("Hide")
else:
    st.write("Seek")

# Radio Button
radio_button = st.radio("Select a color", ("blue", "orange", "yellow"))
st.write(f"You choosed : {radio_button}")

# Button
st.button("Button")

if st.button("Press Me!"):
    st.success("Analyze Results are...")

# Select Box
occupation = st.selectbox("Your occupation", ["Programmer", "DataScientist","Doctor"])
st.write(f"You choosed this occupation : {occupation}")  

# multi select 
multi_select = st.multiselect("Select multiple numbers", [1, 2, 3, 4, 5])

# slider
option1 = st.slider("Select a number", min_value = 5, max_value = 70, value = 30)
# integer başladıysan hepsi integer. float başladyısan hepsi float olmak zorunda.
option2 = st.slider("Select a number", min_value=0.2, max_value=30.2, value=9.0)
result = option1 * option2
st.write("multiplication of two options is", result)

# text_input
name = st.text_input("Enter your name", placeholder="Your name here")
if st.button("Submit"):
    st.write("Hello", name.title())

# code
st.code("import pandas as pd")
st.code("import pandas as pd\nimport numpy as np")

with st.echo():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a" : [1, 2, 3], "b" : [4, 5, 6]})
    df


# date input
import datetime
today = st.date_input("Today is", datetime.datetime.now())

# time input
the_time = st.time_input("The time is", datetime.time(8,45))

# sidebar(very important)
st.sidebar.title("Sidebar title")
st.sidebar.header("Sidebar Header")

a = st.sidebar.slider("input", 0, 5, 2, 1)
x = st.sidebar.slider("input")
st.write("# sidebar input result")
st.success(a*x)
# genelde streamlit'te soldan girdiler alınır sağdan çıktılar verilir.


# Dataframe(important)
st.write("# dataframes")
df = pd.read_csv("Advertising.csv", nrows=(100))
# Dataframe'i 3 yöntemle gösterebilirsiniz:
st.table(df.head()) # 1, static
st.write(df.head()) # 2, dynamic
st.dataframe(df.head()) #3, dynamic

import pickle
filename = "my_model"
model = pickle.load(open(filename, "rb"))
TV = st.sidebar.number_input("TV:",min_value=5, max_value=300)
radio = st.sidebar.number_input("radio:",min_value=1, max_value=50)
newspaper = st.sidebar.number_input("newspaper:",min_value=0, max_value=120)
# Burada slider yerine number_input ile numeric veri alabiliriz.
# Bu 2 yöntemden biri tercih edilir.

my_dict  = {"TV" : TV, "Radio" : radio, "Newspaper" :newspaper}
df=pd.DataFrame.from_dict([my_dict])
st.table(df)


if st.button("Predict"):
    pred = model.predict(df)
    st.write(pred[0])


html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;">Single Customer </h1>
</div><br>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)
st.markdown(html_temp,unsafe_allow_html=True)