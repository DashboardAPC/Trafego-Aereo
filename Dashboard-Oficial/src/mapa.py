import pandas as pd
import plotly.express as  px
import json
import os

#Estrutura do to_dict
# {cabecalho:{id:valor}}

def filtrar(tabela, filtros):
    resultado={}
    for cabecalho in  tabela:
        if cabecalho in filtros:
            resultado[cabecalho]=tabela[cabecalho]
    
    return resultado

estados_brasileiros = json.load(open('Dashboard-Oficial/data/brasil_estados.json'))
voos = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep=';', encoding='latin')
voos_dict = voos.to_dict()
voos_por_estado_dict = filtrar(voos_dict,['AEROPORTO DE DESTINO (UF)','DECOLAGENS'])
voos_por_estado = pd.DataFrame(voos_por_estado_dict)
print(voos_por_estado)

#print(filtrar_estados(voos_dict,['DECOLAGENS','AEROPORTO DE DESTINO (UF)']))
#mapa = px.choropleth(dados_pd, 
 #                   geojson=estados_brasileiros, 
 #                   locations='Estados', 
 #                   color='amor', 
 #                   range_color=(0,1), 
 #                   hover_data =['Estados'], 
 #                   scope='south america')
#mapa.show()