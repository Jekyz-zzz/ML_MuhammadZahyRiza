import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/Jekyz-zzz/ML_MuhammadZahyRiza/main/hour.csv"
df = pd.read_csv(url)

st.title("Bike Sharing Dashboard")

st.subheader("Pola Penggunaan Sepeda Berdasarkan Jam")
fig1, ax1 = plt.subplots()
sns.lineplot(x='hr', y='cnt', data=df, ax=ax1)
st.pyplot(fig1)

st.subheader("Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman")
fig2, ax2 = plt.subplots()
sns.boxplot(x='weathersit', y='cnt', data=df, ax=ax2)
st.pyplot(fig2)

st.subheader("Insight Utama")
st.write("""
- Penggunaan sepeda memuncak pada jam sibuk pagi dan sore hari.
- Kondisi cuaca cerah mendorong peningkatan jumlah peminjaman sepeda.
""")
