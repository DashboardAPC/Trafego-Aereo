import pandas as pd
import math
import plotly.express as px
import tabela_utils


dados = pd.read_csv('https://raw.githubusercontent.com/DashboardAPC/DashboardAPC/master/Dashboard-Oficial/data/ANAC20XX-13-14-15.csv', sep=';', encoding='latin')
filtrado = tabela_utils.filtrar(dados, ['ANO', 'MÊS', 'DECOLAGENS'])

semnulo = tabela_utils.retirar_nulos(filtrado)

ano1 = tabela_utils.fatiar(semnulo, 'ANO', 2013)
ano2 = tabela_utils.fatiar(semnulo, 'ANO', 2014)
ano3 = tabela_utils.fatiar(semnulo, 'ANO', 2015)

ano2013 = tabela_utils.soma_por_categoria(ano1, 'MÊS', 'DECOLAGENS')
ano2014 = tabela_utils.soma_por_categoria(ano2, 'MÊS', 'DECOLAGENS')
ano2015 = tabela_utils.soma_por_categoria(ano3, 'MÊS', 'DECOLAGENS')

ano2013f = tabela_utils.filtrar(ano2013, ['DECOLAGENS'])
ano2014f = tabela_utils.filtrar(ano2014, ['DECOLAGENS'])
ano2015f = tabela_utils.filtrar(ano2015, ['DECOLAGENS'])

ano2013ff = (ano2013f['DECOLAGENS'].to_list())
ano2014ff = (ano2014f['DECOLAGENS'].to_list())
ano2015ff = (ano2015f['DECOLAGENS'].to_list())

anototal = ano2013ff + ano2014ff + ano2015ff

grafico = pd.DataFrame({
    "Mês": ["Janeiro", 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro',"Janeiro", 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro',"Janeiro", 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    "Decolagens": anototal,
    "Ano": ['2013','2013','2013','2013','2013','2013','2013','2013','2013','2013','2013','2013','2014','2014','2014','2014','2014','2014','2014','2014','2014','2014','2014','2014','2015','2015','2015','2015','2015','2015','2015','2015','2015','2015','2015','2015',]
})

fig = px.bar(grafico, x="Mês", y="Decolagens", color="Ano", barmode="group", color_discrete_sequence=px.colors.qualitative.Prism, template='plotly_dark', range_y=[80000,100000])
fig.show()
