import pandas as pd
import plotly.express as px
import streamlit as st

# Cabeçalho da aplicação
st.header('Análise de Anúncios de Vendas de Veículos')

# Carregar os dados (na raiz do projeto)
car_data = pd.read_csv('vehicles.csv')

# Opção com Checkboxes (desafio opcional atendido)
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter:
    st.write('Criando um gráfico de dispersão: Preço vs. Odômetro')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)