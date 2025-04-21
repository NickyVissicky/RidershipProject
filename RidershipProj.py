# Streamlit app
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.dates import DateFormatter, MonthLocator

st.title("ICA on 4/17")

df = pd.read_csv('https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/bike_sharing.csv')

df['dteday'] = pd.to_datetime(df['dteday'])

# 1 -  A line plot of total ridership (column titled cnt) over the course of the entire period.
figure = plt.figure(figsize=(20,10))
plt.plot(df['dteday'], df['cnt'])
plt.xlabel("Date")
plt.ylabel("Total Riders")
plt.title("Total Ridership Over Time")
ax = plt.gca()
ax.xaxis.set_major_locator(MonthLocator(interval=1))
ax.xaxis.set_major_formatter(DateFormatter('%m %y'))
plt.xticks(rotation=45, ha='right')
st.pyplot(figure)

# 2 - A bar plot that shows total ridership by season (season column: 1 = winter, 2 = spring, etc.)
figure2 = plt.figure()
seasons = ['Winter', 'Spring', 'Summer', 'Fall']
plt.bar(seasons, df.groupby('season')['cnt'].sum())
plt.xlabel("Season")
plt.ylabel("Total Riders")
plt.title("Total Ridership by Season")
st.pyplot(figure2)

# 3 - A line plot of total ridership that allows the user to select rolling average.  Using radio buttons, the user may select the following options:
# "7-day average", "14-day average", "Total"
figure3 = plt.figure(figsize=(20,20))

timespan = st.radio("Select a Timespan", ["7-day average", "14-day average", "Week"])
plt.title("Total Ridership Over the " + timespan)

df['7d_avg'] = df['cnt'].rolling(window=7, center=True).mean()
df['14d_avg'] = df['cnt'].rolling(window=14, center=True).mean()

if timespan == '7-day average':
    plt.plot(df['dteday'], df['7d_avg'], label='7-day average')
elif timespan == '14-day average':
    plt.plot(df['dteday'], df['14d_avg'], label='14-day average')
else:
    weekly = df.resample('W', on='dteday').sum()
    plt.plot(weekly.index, weekly['cnt'])

st.pyplot(figure3)
