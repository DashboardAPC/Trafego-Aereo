import math
import pandas as pd
import tabela_utils


dados = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep= ';', encoding= 'latin')
mes_6 = tabela_utils.filtrar_linha(dados, 'MÊS', '6')
mes_6_filtrados = tabela_utils.filtrar(mes_6, ['ANO', 'MÊS', 'AEROPORTO DE ORIGEM (PAÍS)', 'DECOLAGENS'])
mes_6_sem_nulos = tabela_utils.retirar_nulos(mes_6_filtrados)
print(mes_6_sem_nulos)

