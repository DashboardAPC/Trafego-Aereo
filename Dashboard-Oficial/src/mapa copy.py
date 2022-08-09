import pandas as pd
import plotly.express as  px
import json
import os

#Estrutura do to_dict
# {cabecalho:{id:valor}}

def filtrar(tabela: pd.DataFrame, filtros: list) -> pd.DataFrame: 
    """Função feita para filtrar colunas em Dataframes

    Args:
        tabela (pd.DataFrame): A tabela que será filtrada
        filtros (list): Lista de colunas que serão mantidas

    Returns:
        pd.DataFrame: Dataframe com as colunas filtradas
    """
    resultado={}
    tabela = tabela.to_dict()
    for cabecalho in  tabela:
        if cabecalho in filtros:
            resultado[cabecalho]=tabela[cabecalho]
    resultado_pd = pd.DataFrame(resultado)
    return resultado_pd

estados_brasileiros = json.load(open('Dashboard-Oficial/data/brasil_estados.json'))
voos = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep=';', encoding='latin')

voos_por_estado = filtrar(voos,['AEROPORTO DE DESTINO (UF)','DECOLAGENS'])

#print(filtrar_estados(voos_dict,['DECOLAGENS','AEROPORTO DE DESTINO (UF)']))
#mapa = px.choropleth(dados_pd, 
 #                   geojson=estados_brasileiros, 
 #                   locations='Estados', 
 #                   color='amor', 
 #                   range_color=(0,1), 
 #                   hover_data =['Estados'], 
 #                   scope='south america')
#mapa.show()