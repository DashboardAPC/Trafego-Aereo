import math
import pandas as pd
import tabela_utils


dados = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep= ';', encoding= 'latin')
print('Filtrando colunas...')
colunas_filtradas = tabela_utils.filtrar(dados, ['ANO', 'MÊS', 'AEROPORTO DE ORIGEM (PAÍS)', 'DECOLAGENS'])
print('Retirando nulos...')
dados_sem_nulos = tabela_utils.retirar_nulos(colunas_filtradas)
print('Filtrando anos...')
dados_anos = tabela_utils.filtrar_linha(dados_sem_nulos, 'ANO', ['2013', '2014'])
print('Filtrando mês...')
mes_6 = tabela_utils.filtrar_linha(dados_anos, 'MÊS', ['6'])

#filtrando a tabela eliminando todos os dados que não precisaremos

print(mes_6)
