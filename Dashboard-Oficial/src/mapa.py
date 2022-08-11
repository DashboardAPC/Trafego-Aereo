
import pandas as pd
import plotly.express as  px
import json
import tabela_utils


estados_brasileiros = json.load(open('Dashboard-Oficial/data/brasil_estados.json'))
voos = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep=';', encoding='latin')

voos_por_estado = tabela_utils.filtrar(voos,['AEROPORTO DE DESTINO (UF)','DECOLAGENS'])
vpe_nao_nulos = tabela_utils.retirar_nulos(voos_por_estado)
decolagens_por_estado = tabela_utils.soma_por_categoria(vpe_nao_nulos, 'AEROPORTO DE DESTINO (UF)', 'DECOLAGENS')

mapa = px.choropleth(decolagens_por_estado, 
                    geojson=estados_brasileiros, 
                    locations='AEROPORTO DE DESTINO (UF)', 
                    color='DECOLAGENS', 
                    range_color=(0,200000), 
                    hover_data =['AEROPORTO DE DESTINO (UF)'], 
                    scope='south america')
mapa.show()