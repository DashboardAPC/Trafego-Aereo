import math
import pandas as pd
import tabela_utils


tabela = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep=';', encoding='latin')
filtro = tabela_utils.filtrar(tabela, ['ANO', 'MÊS', 'AEROPORTO DE ORIGEM (PAÍS)', 'DECOLAGENS'])


print(filtro.to_string())