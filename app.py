import pandas as pd
import streamlit as st
import plotly_express as px

df_vehicles = pd.read_csv('vehicles_us.csv') #carga los datos del df

st.header('Ventana de datos') #encabezado
# Casilla de verificación
build_df = st.checkbox('Visualizador de datos')
if build_df: #si la casilla está seleccionada...
    # Genera una ventana de visualización interactiva del Dataframe
    df_window = st.dataframe(df_vehicles)

st.header('Densidades por kilometraje')
build_histogram = st.checkbox('¡Hagámos el histograma!')
if build_histogram:
    st.write('Histograma por kilometraje recorrido')
    #crea un histograma
    fig_hist = px.histogram(df_vehicles,
                            x='odometer'
                            )
    #muestra un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

st.header('Relación Precio/Kilometraje')
build_scatter = st.checkbox('¡Veamos la dispersión!')
if build_scatter: #si la casilla está seleccionada...
    st.write('Gráfco de dispersión entre Precio y Kilometraje')
    #crea un gráfico de dispersión
    fig_scatter = px.scatter(df_vehicles,
                             x='odometer',
                             y='price'
                             )
    #muestra un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
