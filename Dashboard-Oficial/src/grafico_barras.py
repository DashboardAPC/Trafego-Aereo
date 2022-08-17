import pandas as pd
import math
import plotly.express as px
import tabela_utils

#FATIA FATIA FATIA FATIA
def fatiar(tabela: pd.DataFrame, cabeçalho_selecionado: str, alvo: int) -> pd.DataFrame:
    tabela = tabela.to_dict()
    fatiador = []
    linha = tabela[cabeçalho_selecionado]
    for id in linha:
        if linha[id] != alvo:
            fatiador.append(id)
    for linha in fatiador:
        for corte in tabela:
            tabela[corte].pop(linha)
    return pd.DataFrame(tabela)

#FAZ TUDO  FAZ TUDO
def faztudo(tabela : pd.DataFrame):
    tabela = tabela_utils.soma_por_categoria(tabela, 'MÊS', 'DECOLAGENS')
    tabela = tabela_utils.filtrar(tabela, ['DECOLAGENS'])
    tabela = (tabela['DECOLAGENS'].to_list())
    return tabela

dados = pd.read_csv('https://raw.githubusercontent.com/DashboardAPC/DashboardAPC/master/Dashboard-Oficial/data/ANAC20XX-13-14-15.csv', sep=';', encoding='latin')
filtrado = tabela_utils.filtrar(dados, ['ANO', 'MÊS', 'DECOLAGENS'])

semnulo = tabela_utils.retirar_nulos(filtrado)

ano1 = fatiar(semnulo, 'ANO', 2013)
ano2 = fatiar(semnulo, 'ANO', 2014)
ano3 = fatiar(semnulo, 'ANO', 2015)

ano2013 = faztudo(ano1)
ano2014 = faztudo(ano2)
ano2015 = faztudo(ano3)

meses = ["Janeiro", 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro', ]*3 #somar o numero de anos
anototal = ano2013 + ano2014 + ano2015 #total de decolagens por ano
anos = ['2013',]*12 +['2014',]*12 + ['2015',]*12 #anos vezes numero de meses

grafico = pd.DataFrame({
    "Mês": meses,
    "Decolagens": anototal,
    "Ano": anos
})
fig = px.bar(grafico, x="Mês", y="Decolagens", color="Ano", barmode="group", color_discrete_sequence=px.colors.qualitative.Prism, template='plotly_dark', range_y=[80000,100000])
fig.show()