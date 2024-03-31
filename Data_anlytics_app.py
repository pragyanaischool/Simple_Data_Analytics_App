import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('My Data Analytics App')  # Sets the title of your page

st.subheader('Data Loading Section')  # Sets a header for a section

# Loading data from URL
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv'
df = pd.read_csv(url, parse_dates=['Date'])

# Display DataFrame in Streamlit
st.dataframe(df)

st.text(df.info())

st.write(df.describe())
