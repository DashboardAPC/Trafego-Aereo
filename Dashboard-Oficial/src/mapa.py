# ----------------------------------------- Importando bibliotecas -----------------------------------------
import pandas as pd
import plotly.express as px
import tabela_utils
import json


# --------------------------------------- Criando geometria do Brasil ---------------------------------------
print('Lendo geometria...') # Feedback
estados_brasileiros = json.load(open('Dashboard-Oficial/data/brasil_estados.json'))


# ---------------------------------------------- Lendo dataset ----------------------------------------------
print('Lendo dataset...') # Feedback
dados = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep = ';', encoding = 'latin') # Encoding sendo usado para evitar problemas com acentuação


# --------------------------------------- Manipulando dados necessarios---------------------------------------
print('Filtrando colunas...') # Feedback
voos = tabela_utils.filtrar(dados,['AEROPORTO DE DESTINO (UF)','DECOLAGENS'])

print('Retirando valores nulos...') # Feedback
voos = tabela_utils.retirar_nulos(voos)

print('Somando por categoria...')
voos = tabela_utils.soma_por_categoria(voos, 'AEROPORTO DE DESTINO (UF)', 'DECOLAGENS')

print('Calculando valor máximo...') # Feedback
maximo_decolagens = tabela_utils.maximo(voos, 'DECOLAGENS')


# ------------------------------------------ Criando gráfico de mapa ------------------------------------------
print('Produzindo mapa...') # Feedback
mapa = px.choropleth(voos,
                    template = 'plotly_dark',
                    geojson = estados_brasileiros, 
                    locations = 'AEROPORTO DE DESTINO (UF)', 
                    color = 'DECOLAGENS', 
                    range_color = (0,maximo_decolagens/4), 
                    hover_data = ['AEROPORTO DE DESTINO (UF)'], 
                    scope = 'south america',
                    color_continuous_scale = 'purp'
                    )


# ----------------------------------------- Mostrando gráfico de mapa -----------------------------------------
print('Mostrando mapa...') # Feedback
mapa.show()