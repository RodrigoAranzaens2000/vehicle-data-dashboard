import pandas as pd
import plotly.express as px
import streamlit as st

# Leer datos
data = pd.read_csv('vehicles_us.csv')

# Título
st.title("Panel de Control de Anuncios de Vehículos")

# Histograma de precios
st.header("Distribución de Precios")
fig = px.histogram(data, x="price")
st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión precio vs año 
st.header("Precio vs Año")
fig = px.scatter(data, x="model_year", y="price")
st.plotly_chart(fig, use_container_width=True)

# Histograma de precios
st.header("Distribución de Precios")
show_hist = st.checkbox("Mostrar Histograma de Precios")
if show_hist:
    fig = px.histogram(data, x="price")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión precio vs año
st.header("Precio vs Año") 
show_scatter = st.checkbox("Mostrar Gráfico de Dispersión Precio vs Año")
if show_scatter:
    fig = px.scatter(data, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True)