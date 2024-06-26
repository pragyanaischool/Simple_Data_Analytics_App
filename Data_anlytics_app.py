import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.figure_factory as ff
from sklearn.preprocessing import LabelEncoder

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

st.subheader('Count Plot: For Class / Target')
fig1, ax1 = plt.subplots()
survived = df_titanic['Survived'].value_counts()[1]
not_survived = df_titanic['Survived'].value_counts()[0]
survived_per = survived / df_titanic.shape[0] * 100
not_survived_per = not_survived / df_titanic.shape[0] * 100

plt.figure(figsize=(10, 8))

plt.xlabel('Survival', size=15, labelpad=15)
plt.ylabel('Passenger Count', size=15, labelpad=15)
plt.xticks((0, 1), ['Not Survived ({0:.2f}%)'.format(not_survived_per), 'Survived ({0:.2f}%)'.format(survived_per)])
plt.tick_params(axis='x', labelsize=13)
plt.tick_params(axis='y', labelsize=13)

plt.title('Training Set Survival Distribution', size=15, y=1.05)
sns.countplot(data = df_titanic, x = "Survived", ax = ax1)
st.pyplot(fig1)


st.subheader('HeatMAP: ')
# Basic Data Cleaning is Essential
df_train = df_titanic.drop(['PassengerId'], axis=1)
df_train.dropna(inplace =True)
df_train.drop_duplicates(inplace =True)

plot = sns.heatmap(df_train.corr(numeric_only=True),  annot=True, square=True, cmap='coolwarm', annot_kws={'size': 14})
st.pyplot(plot.get_figure())

st.subheader('PairPlot: ')

# Encoding Categorical values

df_train.drop(['Name'], axis=1, inplace = True)

non_numeric_features = ['Embarked', 'Sex', 'Cabin',  'Ticket']

for feature in non_numeric_features:        
        df_train[feature] = LabelEncoder().fit_transform(df_train[feature])

# Create a Seaborn pairplot
plot1 = sns.pairplot(df_train)
 
# Display the plot in Streamlit
st.pyplot(plot1.fig)


st.dataframe(df_train)
#fig2, axs = plt.subplots( figsize=(50, 50))

#sns.heatmap(df_train.corr(numeric_only=True), ax=axs, annot=True, square=True, cmap='coolwarm', annot_kws={'size': 14})
    
#axs.set_title('Titanic DataSet Correlations', size=15)

#st.pyplot(fig2)
