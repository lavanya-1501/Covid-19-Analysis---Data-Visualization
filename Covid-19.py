import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.write('# COVID-19 Analysis')
st.markdown('Statewise **COVID 19 Cases** Analytic Report on _25-04-2021_ in India Using various charts')


st.header('Dataset')
@st.cache
def load_data(path):
    dataset = pd.read_csv(path)
    return dataset

df=pd.read_csv('graphs.csv')
st.dataframe(df, 1500, 1000)

df = df.sort_values(by=['Confirmed'],ascending=False)




#Bar Plot
st.header('Bar Plot')
fig,ax = plt.subplots()
w = 0.25
bar1=plt.bar(df['State'][:15], df['Confirmed'][:15],label='Confirmed', align='center',color='b')
bar2=plt.bar(df['State'][:15], df['Cured'][:15],label='Cured',align='center',color='g')
bar3=plt.bar(df['State'][:15], df['Deaths'][:15],label='Deaths', align='center',color='r')
r1 = np.arange(len(df['State']))[:15]
r2 = [x + w for x in r1]
r3 = [x + w for x in r2]
labels = df['State'][:15]
plt.legend()
bars=bar1+bar2+bar3
for re in bars:
    height=re.get_height()
    plt.text(re.get_x()+re.get_width()/2.0,height,height,fontsize=6, ha='center', va='bottom',fontweight='bold',color='black')
plt.ylabel('Number of Confirmed Cases')
plt.xticks(rotation = 70)
plt.title('States with maximum confirmed cases, cures and deaths')
st.pyplot(fig)


#Histogram
st.header('Histogram')
fig,ax = plt.subplots()
plt.hist(df['Confirmed'], bins=6, fc='Blue', ec='white')
plt.xlabel('Confirmed Cases')
plt.ylabel('Count of States')
plt.title('Count of States with maximum confirmed cases')
st.pyplot(fig)


#Scatter Plot
st.header('Scatter Plot')
fig,ax = plt.subplots()
plt.scatter(df['State'][:15], df['Confirmed'][:15],color='b', label='Confirmed')
plt.scatter(df['State'][:15], df['Cured'][:15],color='g',label='Cured')
plt.scatter(df['State'][:15], df['Deaths'][:15],color='r',label='Deaths')
plt.legend()
plt.ylabel('Number of Cases')
plt.xticks(rotation = 70)
plt.title('States with maximum confirmed cases, cures and deaths')
st.pyplot(fig)


#Area Plot
st.header('Area Plot')
fig,ax = plt.subplots()
plt.plot([], [], color='b', label='Confirmed', linewidth=5)
plt.plot([], [], color='g', label='Cured', linewidth=5)
plt.plot([], [], color='r', label='Deaths', linewidth=5)
plt.stackplot(df['State'][:15], df['Confirmed'][:15], df['Cured'][:15], df['Deaths'][:15], colors=['b', 'g', 'r'])
plt.ylabel('Number of Cases')
plt.xticks(rotation=70)
plt.title('States with maximum confirmed cases, cures and deaths')
plt.legend()
st.pyplot(fig)