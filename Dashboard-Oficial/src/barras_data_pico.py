# ----------------------------------------- Importando bibliotecas -----------------------------------------
import pandas as pd
import plotly.express as px
import tabela_utils


# ------------------------------------------- Funções Específicas -------------------------------------------
def faztudo(tabela : pd.DataFrame):
    tabela = tabela_utils.soma_por_categoria(tabela, 'MÊS', 'DECOLAGENS')
    tabela = tabela_utils.filtrar(tabela, ['DECOLAGENS'])
    tabela = (tabela['DECOLAGENS'].to_list())
    return tabela


# ---------------------------------------------- Lendo dataset ----------------------------------------------
print('Lendo dataset...') # Feedback
dados = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep = ';', encoding = 'latin') # Encoding sendo usado para evitar problemas com acentuação


# --------------------------------------- Manipulando dados necessarios---------------------------------------
print('Filtrando os dados...') # Feedback
filtrado = tabela_utils.filtrar(dados, ['ANO', 'MÊS', 'DECOLAGENS'])

print('Retirando os nulos...') # Feedback
semnulo = tabela_utils.retirar_nulos(filtrado)
ano1 = tabela_utils.fatiar(semnulo, 'ANO', 2013)
ano2 = tabela_utils.fatiar(semnulo, 'ANO', 2014)
ano3 = tabela_utils.fatiar(semnulo, 'ANO', 2015)

print('Fazendo mágica...') # Feedback
ano2013 = faztudo(ano1)
ano2014 = faztudo(ano2)
ano2015 = faztudo(ano3)

meses = ["Janeiro", 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']*3 #somar o numero de anos
anototal = ano2013 + ano2014 + ano2015 #total de decolagens por ano
anos = ['2013']*12 +['2014']*12 + ['2015']*12 #anos vezes numero de meses


grafico = pd.DataFrame({
    "Mês": meses,
    "Decolagens": anototal,
    "Ano": anos
})


# ----------------------------------------- Criando gráfico de barras -----------------------------------------
print('Produzindo gráfico...') # Feedback
fig = px.bar(grafico, 
            x = "Mês", 
            y = "Decolagens", 
            color = "Ano", 
            barmode = "group", 
            color_discrete_sequence = px.colors.qualitative.Prism, 
            template = 'plotly_dark', 
            range_y = [80000,100000], 
            title = 'Total de decolagens por mês'
            )

# ---------------------------------------- Mostrando gráfico de barras ----------------------------------------
print('Mostrando gráfico...') # Feedback
fig.show()