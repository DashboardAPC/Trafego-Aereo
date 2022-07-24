import pandas as pd

df = pd.read_csv('obitos-confirmados-covid-19.csv')
print(df['MUNICIPIO_RESIDENCIA'].value_counts())