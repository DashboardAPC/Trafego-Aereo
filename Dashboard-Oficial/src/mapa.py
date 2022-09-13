# ----------------------------------------- Importando bibliotecas -----------------------------------------
import pandas as pd
import plotly.express as px
import tabela_utils
import json
# Testes WSL

# --------------------------------------- Criando geometria do Brasil ---------------------------------------
print('mapa - Lendo geometria...') # Feedback
estados_brasileiros = json.load(open('Dashboard-Oficial/data/brasil_estados.json'))
# ---------------------------------------------- Lendo dataset ----------------------------------------------
print('mapa - Lendo dataset...') # Feedback
dados = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep = ';', encoding = 'latin') # Encoding resolve problema da acentuação

def criar_mapa(ano='2013', estado='DF'):
    # --------------------------------------- Manipulando dados necessarios---------------------------------------
    print('mapa - filtrando linhas')
    mapa = tabela_utils.filtrar_linhas(dados,[ano])

    print('mapa - Filtrando colunas...') # Feedback
    mapa = tabela_utils.filtrar_colunas(dados, ['AEROPORTO DE DESTINO (UF)', 'DECOLAGENS'])

    print('mapa - Retirando valores nulos...') # Feedback
    mapa = tabela_utils.retirar_nulos(mapa)

    print('mapa - Somando por categoria...') # Feedback
    mapa = tabela_utils.soma_por_categoria(mapa, 'AEROPORTO DE DESTINO (UF)', 'DECOLAGENS')

    print('mapa - Calculando valor máximo...') # Feedback
    maximo_decolagens = tabela_utils.maximo(mapa , 'DECOLAGENS')

    # ------------------------------------------ Criando gráfico de mapa ------------------------------------------
    print('mapa - Produzindo mapa...') # Feedback
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
