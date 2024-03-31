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

df = pd.read_csv(url, parse_dates=['Date'])
st.write("Histogram Plot")
# Plot histogram
feature = "Temp"
fig, ax = plt.subplots()
ax.hist(df[feature], bins=20)
# Set the title and labels
ax.set_title(f'Histogram of {feature}')
ax.set_xlabel(feature)
ax.set_ylabel('Frequency')

# Display the plot
st.pyplot(fig)

# Plotting a histogram
st.subheader('Histogram: with Seaborn')
fig, ax = plt.subplots()
plt.figure(figsize=(10,6))
sns.histplot(data=df, x=feature, kde=True, ax =ax)
st.pyplot(fig)

st.header('Data Visualization of Titanic Data')  # Sets a header for a section
# Load the Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df_titanic = pd.read_csv(url)
st.dataframe(df_titanic)
