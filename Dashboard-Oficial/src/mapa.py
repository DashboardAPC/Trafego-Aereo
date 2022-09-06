# ----------------------------------------- Importando bibliotecas -----------------------------------------
import pandas as pd
import plotly.express as px
import tabela_utils
import json


# --------------------------------------- Criando geometria do Brasil ---------------------------------------
print('3 - Lendo geometria...') # Feedback
estados_brasileiros = json.load(open('Dashboard-Oficial/data/brasil_estados.json'))


# ---------------------------------------------- Lendo dataset ----------------------------------------------
print('3 - Lendo dataset...') # Feedback
dados = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep = ';', encoding = 'latin') # Encoding resolve problema da acentuação


# --------------------------------------- Manipulando dados necessarios---------------------------------------
print('3 - Filtrando colunas...') # Feedback
dados = tabela_utils.filtrar_colunas(dados, ['AEROPORTO DE DESTINO (UF)', 'DECOLAGENS'])

print('3 - Retirando valores nulos...') # Feedback
dados = tabela_utils.retirar_nulos(dados)

print('3 - Somando por categoria...') # Feedback
dados = tabela_utils.soma_por_categoria(dados, 'AEROPORTO DE DESTINO (UF)', 'DECOLAGENS')

print('3 - Calculando valor máximo...') # Feedback
maximo_decolagens = tabela_utils.maximo(dados, 'DECOLAGENS')


# ------------------------------------------ Criando gráfico de mapa ------------------------------------------
print('3 - Produzindo mapa...') # Feedback
grafico_mapa = px.choropleth(dados,
                    template = 'plotly_dark',
                    geojson = estados_brasileiros, 
                    locations = 'AEROPORTO DE DESTINO (UF)', 
                    color = 'DECOLAGENS', 
                    range_color = (0, maximo_decolagens/4), # Resolve problema de SP ser o unico estado colorido
                    hover_data = ['AEROPORTO DE DESTINO (UF)'], 
                    scope = 'south america',
                    color_continuous_scale = 'purp',
                    title = 'Estados de destino mais escolhidos'
                    )