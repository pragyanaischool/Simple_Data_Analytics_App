import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.figure_factory as ff

st.title('My Data Analytics App')  # Sets the title of your page

st.subheader('Data Loading Section')  # Sets a header for a section

# Loading data from URL
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv'
df = pd.read_csv(url, parse_dates=['Date'])

# Display DataFrame in Streamlit
st.dataframe(df)

st.write("Basic Analytics")

#txt = df.info()
#st.text(txt)

st.write(df.describe())

st.write("Line Chart")
# Display line chart
st.line_chart(df.set_index('Date'))

st.write("Histogram Plot")
fig = ff.create_distplot(df['Temp'], "Temp")
st.plotly_chart(fig, use_container_width=True)
