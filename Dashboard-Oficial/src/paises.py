import math
from re import A
import pandas as pd
import tabela_utils
import plotly.express as px


dados = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep= ';', encoding= 'latin')
print('Filtrando colunas...')
colunas_filtradas = tabela_utils.filtrar(dados, ['ANO', 'MÊS', 'AEROPORTO DE ORIGEM (PAÍS)', 'DECOLAGENS'])
print('Retirando nulos...')
dados_sem_nulos = tabela_utils.retirar_nulos(colunas_filtradas)
print('Filtrando anos...')
dados_anos = tabela_utils.filtrar_linha(dados_sem_nulos, 'ANO', ['2013', '2014'])
print('Filtrando mês...')
mes_6 = tabela_utils.filtrar_linha(dados_anos, 'MÊS', ['6'])
print('Filtrando países...')
dados_paises = tabela_utils.filtrar_linha(mes_6, 'AEROPORTO DE ORIGEM (PAÍS)', ['ESTADOS UNIDOS DA AMÉRICA', 'MÉXICO', 'ARGENTINA', 'REINO UNIDO', 'EMIRADOS ÁRABES UNIDOS'] )
#print(dados_paises)
print('Filtrando o ano de 2013...')
dados_2013 = tabela_utils.filtrar_linha(dados_paises, 'ANO', ['2013'])
print('Somando...')
soma_2013 = tabela_utils.soma_por_categoria(dados_2013, 'AEROPORTO DE ORIGEM (PAÍS)', 'DECOLAGENS')
print('Filtrando o ano de 2014...')
dados_2014 = tabela_utils.filtrar_linha(dados_paises, 'ANO', ['2014'])
print('Somando...')
soma_2014 = tabela_utils.soma_por_categoria(dados_2014, 'AEROPORTO DE ORIGEM (PAÍS)', 'DECOLAGENS')

def faztudo(tabela : pd.DataFrame):
    tabela = tabela_utils.soma_por_categoria(dados_2014, 'AEROPORTO DE ORIGEM (PAÍS)', 'DECOLAGENS')
    tabela = tabela_utils.filtrar(tabela, ['DECOLAGENS'])
    tabela = (tabela['DECOLAGENS'].to_list())
    return tabela
ano2013 = faztudo(soma_2013)
ano2014 = faztudo(soma_2014)
print(ano2013)
print(ano2014)
aeroporto = ['ESTADOS UNIDOS DA AMÉRICA', 'MÉXICO', 'ARGENTINA', 'REINO UNIDO', 'EMIRADOS ÁRABES UNIDOS']*2
decolagens = ano2013 + ano2014
anos = ['2013',]*5 +['2014',]*5 

grafico = pd.DataFrame({
    "Mês": aeroporto,
    "Decolagens": decolagens,
    "Ano": anos
})

fig = px.bar(grafico, x="Mês", y="Decolagens", color="Ano", barmode="group", color_discrete_sequence=px.colors.qualitative.Prism, template='plotly_dark')
fig.show()