import pandas as pd
import streamlit as st
import plotly_express as px

df_vehicles = pd.read_csv('vehicles_us.csv') #carga los datos del df

st.header('Aplicación de vehículos') #encabezado
scatter_button = st.button('Generar Dispersión') #crea un botón para ejecutar el código del grafico de dispersión
hist_button = st.button('Generar Histograma') #crea un botón para ejecutar el código del histograma


if hist_button: # al hacer clic en el botón
    # escribe un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    #crea un histograma
    fig_hist = px.histogram(df_vehicles,
                            x='odometer'
                            )
    #muestra un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

if scatter_button:
    
    st.write('Creación de gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # crea un gráfico de dispersión
    fig_scatter = px.scatter(df_vehicles,
                             x='odometer',
                             y='price'
                             )
    #muestra el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)

