import imp
import streamlit as st
import pandas as pd
import yfinance as yf

st.write(""" 
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Apple!
""")

tickerSymbol = "AAPL"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = "1d", start = "2010-5-31", end = "2022-9-16")

st.write("Closing Price")
st.line_chart(tickerDf.Close)
st.write("Volume Price")
st.line_chart(tickerDf.Volume)

