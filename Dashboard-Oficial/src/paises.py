import math
import pandas as pd
import tabela_utils


tabela = pd.read_csv('C:\UnB\APC\DashboardAPC\Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep=';')

print(tabela.to_string())