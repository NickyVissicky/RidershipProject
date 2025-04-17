import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/bike_sharing.csv')

df['datetime'] = pd.to_datetime(df['dteday'])

st.header("Total Ridership Over Time (Count)")

fig, ax = plt.subplots()
ax.plot(df['datetime'], df['cnt'])
ax.set_xlabel("Date")
ax.set_ylabel("Total Riders")
ax.set_title("Total Ridership")
st.pyplot(fig)

fig, ax = plt.subplots()
ax.plot(df['dteday'], df['cnt'])
ax.set_xlabel("Date")
ax.set_ylabel("Total Riders")
ax.set_title("Total Ridership Over Time")

st.header("Total Ridership by Season")

fig2, ax2 = plt.subplots()
seasons = ['Winter', 'Spring', 'Summer', 'Fall']
ax2.bar(seasons, df.groupby('season')['cnt'].sum())
ax2.set_xlabel("Season")
ax2.set_ylabel("Total Riders")
ax2.set_title("Total Ridership by Season")
st.pyplot(fig2)

choices = ["7-Day Average", "14-Day Average", "Total by week"]

st.header("Rolling Average of Riders (7d, 14d, Weekly)")
option = st.radio("Select a Rolling Average", choices)

df['7d_avg'] = df['cnt'].rolling(window=7, center=True).mean()
df['14d_avg'] = df['cnt'].rolling(window=14, center=True).mean()

if option == choices[0]:
  plt.plot(df['datetime'], df['7d_avg'])
elif option == choices[1]:
  plt.plot(df['datetime'], df['7d_avg'])
  
