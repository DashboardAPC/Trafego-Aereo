import pandas as pd
import plotly.express as px

df = pd.read_csv('obitos-confirmados-covid-19.csv')
qtd_data = df['DATA_OBITO'].value_counts()
obitos_por_data = pd.DataFrame(
    {'DATA':qtd_data.index, 'QUANTIDADE':qtd_data.values}
)
obitos_por_data['DATA'] = pd.to_datetime(obitos_por_data['DATA'], infer_datetime_format=True)
obitos_por_data = obitos_por_data.sort_values(by='DATA')
fig = px.line(obitos_por_data, x='DATA', y = 'QUANTIDADE', title='Óbitos por data em um estado')
fig.show()
