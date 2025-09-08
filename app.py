import pandas as pd
import streamlit as st
import plotly_express as px

df_vehicles = pd.read_csv('vehicles_us.csv') #carga los datos del df

st.header('Aplicación de vehículos') #encabezado
# crea casillas de verificación
build_histogram = st.checkbox('¡Hagámos un histograma!')
build_scatter = st.checkbox('¡Veamos la dispersión!')

if build_histogram: #si la casilla está seleccionada...
    st.write('Construiremos un histograma para la columna odómetro')
    #crea un histograma
    fig_hist = px.histogram(df_vehicles,
                            x='odometer'
                            )
    #muestra un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter: #si la casilla está seleccionada...
    st.write('Construiremos un gráfico de dispersión para las columnas odómetro y price')
    #crea un gráfico de dispersión
    fig_scatter = px.scatter(df_vehicles,
                             x='odometer',
                             y='price'
                             )
    #muestra un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
