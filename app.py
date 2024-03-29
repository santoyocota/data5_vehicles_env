import streamlit as st
import pandas as pd
import plotly_express as px
import os

try:
    os.system("cls")
    data = pd.read_csv('vehicles_us.csv')

except Exception:
    print("An exception occurred")
    print(f"{Exception}")


st.header('Análisis de datos de anuncios de venta de coches')
hist_button = st.checkbox('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


dispersion_button = st.checkbox(
    'Construir gráfico de dispersión')  # crear un botón

if dispersion_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.scatter(data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
