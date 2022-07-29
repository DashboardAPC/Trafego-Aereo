import pandas as pd
import plotly.express as px

#Ler arquivo csv e transformar em DataFrame
df = pd.read_csv('obitos-confirmados-covid-19.csv')

#Contar óbitos por data e transformar Série em dataframe para uso com plotly
qtd_data = df['DATA_OBITO'].value_counts()
obitos_por_data = pd.DataFrame({'DATA':qtd_data.index, 'QUANTIDADE':qtd_data.values})

#Transformar campo DATA em objeto de data python para ogranizar datas de forma crescente
obitos_por_data['DATA'] = pd.to_datetime(obitos_por_data['DATA'], infer_datetime_format=True)
obitos_por_data = obitos_por_data.sort_values(by='DATA')

#Usar DataFrame de óbitos por data para montar um gráfico de linha  e mostrár-lo (Não sou bom de português)
fig = px.line(obitos_por_data, x='DATA', y = 'QUANTIDADE', title='Óbitos por data em um estado')
fig.show()
