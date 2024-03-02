import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

sns.set(style='dark')

alldata = pd.read_csv("/mount/src/dashboard-proyek-akhir-belajar-analisis-data-dicoding/dashboard/day.csv")

st.title("Bike Share Dashboard")

# SIDEBAR
st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Birgita Putri Grania Effendi**")
st.sidebar.markdown(
    "**• Email: birgitaeffendi@gmail.com**")
st.sidebar.markdown(
    "**• ID Dicoding: grania**")

st.sidebar.title("Dataset Bike Share")

#dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(alldata)

#statistik
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(alldata.describe())

# Dataset Source
st.sidebar.markdown("[Download Dataset](https://drive.google.com/drive/folders/10qk4e7ZwtC_6etRil0GZ8-bCJOWZcsY2?usp=drive_link)")

st.sidebar.markdown('**Weather:**')
st.sidebar.markdown('1: Clear, Few clouds, Partly cloudy, Partly cloudy')
st.sidebar.markdown('2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist')
st.sidebar.markdown('3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds')
st.sidebar.markdown('4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog')

st.sidebar.markdown('**Season:**')
st.sidebar.markdown('1: Spring')
st.sidebar.markdown('2: Summer')
st.sidebar.markdown('3: Fall')
st.sidebar.markdown('4: Winter')

correlation_temp_registered = alldata['temp'].corr(alldata['registered'])
st.subheader("Hubungan Bike Sharing dengan Cuaca dan Musim")
#temp dengan registered
fig1, ax1 = plt.subplots(figsize=(12, 8))
ax1.scatter(alldata['temp'], alldata['registered'])
ax1.set_title('Hubungan Antara Temperatur dan Jumlah Pengguna Terdaftar dengan Korelasi: {:.2f}'.format(correlation_temp_registered))
ax1.set_xlabel('Temperatur')
ax1.set_ylabel('Jumlah Pengguna Terdaftar')
st.pyplot(fig1)

#weathersit dengan cnt per musim
fig2, ax2 = plt.subplots(figsize=(12, 8))
sns.barplot(x='weathersit', y='cnt', hue='season', data=alldata, palette='viridis')
ax2.set_title('Hubungan Antara Cuaca dan Jumlah Sewa Sepeda per Musim')
ax2.set_xlabel('Cuaca (weathersit)')
ax2.set_ylabel('Jumlah Sewa Sepeda')
ax2.legend(title='Musim')
st.pyplot(fig2)

#perbandingan cnt di musim panas ketika holiday dan hari biasa divisualisasikan dengan bar plot
holiday = alldata[(alldata['holiday'] == 1) & (alldata['season'] == 2) & ((alldata['yr'] == 0) | (alldata['yr'] == 1))]
total_holiday = holiday['cnt'].sum()

non_holiday = alldata[(alldata['holiday'] == 0) & (alldata['season'] == 2) & ((alldata['yr'] == 0) | (alldata['yr'] == 1))]
total_non_holiday = non_holiday['cnt'].sum()

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.5

bar1 = ax.bar(0, total_holiday, bar_width, label='Holiday', color='blue')
bar2 = ax.bar(1, total_non_holiday, bar_width, label='Non-Holiday', color='orange')

ax.bar(1, total_non_holiday, bar_width, color='red', alpha=0.3)
ax.text(0, total_holiday + 100, str(total_holiday), ha='center', va='bottom')
ax.text(1, total_non_holiday + 100, str(total_non_holiday), ha='center', va='bottom')
ax.set_xticks([0, 1])
ax.set_xticklabels(['Holiday', 'Non-Holiday'])
ax.set_ylabel('Total Sewa Sepeda (cnt)')
ax.set_title('Perbandingan Total Sewa Sepeda pada Hari Libur dan Hari Biasa selama Musim Panas (2011-2012)')
st.pyplot(fig)
