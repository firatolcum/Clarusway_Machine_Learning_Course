import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

st.slider("frt", 5, 20, 10)
st.sidebar.slider("srt", 10, 100, 50)
st.sidebar.number_input("num input", 0, 23, 10)