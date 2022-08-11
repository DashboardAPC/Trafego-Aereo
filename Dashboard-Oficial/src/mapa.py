
import pandas as pd
import plotly.express as  px
import json
import tabela_utils


estados_brasileiros = json.load(open('Dashboard-Oficial/data/brasil_estados.json'))
voos = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep=';', encoding='latin')

voos_por_estado = tabela_utils.filtrar(voos,['AEROPORTO DE DESTINO (UF)','DECOLAGENS'])
vpe_nao_nulos = tabela_utils.retirar_nulos(voos_por_estado)

#mapa = px.choropleth(dados_pd, 
 #                   geojson=estados_brasileiros, 
 #                   locations='Estados', 
 #                   color='amor', 
 #                   range_color=(0,1), 
 #                   hover_data =['Estados'], 
 #                   scope='south america')
#mapa.show()