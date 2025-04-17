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