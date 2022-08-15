import math
import pandas as pd
import tabela_utils


trafego = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep= ';', encoding= 'latin')
#filtro = tabela_utils.filtrar(trafego,['ANO', 'MÊS', 'AEROPORTO DE ORIGEM (PAÍS)', 'DECOLAGENS'])
#trafego.loc[trafego('ANO')<2015]
print(trafego['ANO'])#nesta linha eu pego apenas a coluna ANO e imprimo

