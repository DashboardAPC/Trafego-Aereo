# ----------------------------------------- Importando bibliotecas -----------------------------------------
import pandas as pd
import plotly.express as px
import tabela_utils
import json
from pathlib import Path

data = Path('Dashboard-Oficial/data/')
print('mapa - Lendo geometria...') # Feedback
estados_brasileiros = json.load(open(data / 'brasil_estados.json'))

# ---------------------------------------------- Lendo dataset ----------------------------------------------
print('mapa - Lendo dataset...') # Feedback
dados = pd.read_csv(data / 'ANAC20XX-13-14-15.csv', sep = ';', encoding = 'latin') # Encoding resolve problema da acentuação

print('mapa - Lendo coordenadas...')
coords = pd.read_csv(data / 'coord-estados.csv')

def criar_lista_dropdowns():
    resultado=[]
    valores_coordenadas=coords.values.tolist()
    for linha in valores_coordenadas:
        resultado.append(linha[0])
    return sorted(resultado)

def ler_coordenadas(tabela : pd.DataFrame, estado: str):
    valores = tabela.values.tolist()
    resultado = {'lat':0,'lon':0}
    for linha in valores:
        if linha[0]==estado:
            resultado['lat']=linha[1]
            resultado['lon']=linha[2]
    return resultado

def criar_mapa(ano='2013', estado='DF'):
    # --------------------------------------- Manipulando dados necessarios---------------------------------------
    print('mapa - filtrando linhas')
    mapa = tabela_utils.filtrar_linhas(dados,'ANO',[ano])

    print('mapa - Filtrando colunas...') # Feedback
    mapa = tabela_utils.filtrar_colunas(mapa, ['AEROPORTO DE DESTINO (UF)', 'DECOLAGENS'])

    print('mapa - Retirando valores nulos...') # Feedback
    mapa = tabela_utils.retirar_nulos(mapa)

    print('mapa - Somando por categoria...') # Feedback
    mapa = tabela_utils.soma_por_categoria(mapa, 'AEROPORTO DE DESTINO (UF)', 'DECOLAGENS')

    print('mapa - Calculando valor máximo...') # Feedback
    maximo_decolagens = tabela_utils.maximo(mapa , 'DECOLAGENS')

    # ------------------------------------------ Criando gráfico de mapa ------------------------------------------
    print('mapa - Produzindo mapa...') # Feedback
    grafico_mapa = px.choropleth_mapbox(mapa,
                        mapbox_style='carto-positron',
                        zoom=5,
                        center=ler_coordenadas(coords,estado),
                        geojson = estados_brasileiros, 
                        locations = 'AEROPORTO DE DESTINO (UF)', 
                        color = 'DECOLAGENS', 
                        range_color = (0, maximo_decolagens/4), # Resolve problema de SP ser o unico estado colorido
                        hover_data = ['AEROPORTO DE DESTINO (UF)'], 
                        color_continuous_scale = 'purp',
                        title = 'Estados de destino mais escolhidos',
                        )

    return grafico_mapa

if __name__=="__main__":
    meu_mapa = criar_mapa()
    meu_mapa.show()
