import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from PIL import Image

def run():
    # Buat title
    st.title('EDA TEST')

    # Membuat Subheader
    st.subheader('Page ini dibuat oleh *Rizqullah*')

    # Menambahkan teks
    st.write('# Biji onta')
    st.write('## Biji onta')
    st.write('### Biji onta')
    st.write('#### Biji onta')

    # Menambahkan gambar
    image_data = Image.open('images.png')
    st.image(image_data, caption='my jurusan')

    # Menambahkan dataframe
    df = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/refs/heads/v2.3/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    st.dataframe(df)

    # Menambahkan plot
    st.write('Histogram')
    fig1 = plt.figure(figsize=(15,5))
    sns.histplot(df['Overall'], bins=30, kde=True)
    st.pyplot(fig1)

    # Plot Interaktif (Sesuai Input User)
    st.write('Histogram')
    opsi = st.selectbox('Column', ('Age', 'Height', 'Weight', 'ShootingTotal'))
    fig2 = plt.figure(figsize=(15,5))
    sns.histplot(df[opsi], bins=30, kde=True)
    st.pyplot(fig2)

    # Membuat plotlyplot
    st.write('PlotlyPlot - Overall vs ValueEUR')
    fig3 = px.scatter(df, x='ValueEUR', y='Overall', hover_data=['Name', 'Age'])
    st.plotly_chart(fig3)

if __name__ == '__main__': 
    run()