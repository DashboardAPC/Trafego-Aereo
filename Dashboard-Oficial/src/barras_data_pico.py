# ----------------------------------------- Importando bibliotecas -----------------------------------------
import pandas as pd
import plotly.express as px
import tabela_utils


# ------------------------------------------- Funções Específicas -------------------------------------------
def faztudo(tabela : pd.DataFrame):
    tabela = tabela_utils.soma_por_categoria(tabela, 'MÊS', 'DECOLAGENS')
    tabela = tabela_utils.filtrar_colunas(tabela, ['DECOLAGENS'])
    tabela = (tabela['DECOLAGENS'].to_list())
    return tabela


# ---------------------------------------------- Lendo dataset ----------------------------------------------
print('Lendo dataset...') # Feedback
dados = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep = ';', encoding = 'latin') # Encoding resolve problema da acentuação


# --------------------------------------- Manipulando dados necessarios---------------------------------------
print('Filtrando os dados...') # Feedback
filtrado = tabela_utils.filtrar_colunas(dados, ['ANO', 'MÊS', 'DECOLAGENS'])

print('Retirando os nulos...') # Feedback
sem_nulo = tabela_utils.retirar_nulos(filtrado)

print('Separando anos...') # Feedback
ano_1 = tabela_utils.filtrar_linhas(sem_nulo, 'ANO', '2013.0')
ano_2 = tabela_utils.filtrar_linhas(sem_nulo, 'ANO', '2014.0')
ano_3 = tabela_utils.filtrar_linhas(sem_nulo, 'ANO', '2015.0')

print('Fazendo mágica...') # Feedback
ano_2013 = faztudo(ano_1)
ano_2014 = faztudo(ano_2)
ano_2015 = faztudo(ano_3)


# --------------------------------------------- Criando Dataframe ---------------------------------------------
ano_total = ano_2013 + ano_2014 + ano_2015
meses = ["Janeiro", 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']*3
anos = ['2013']*12 + ['2014']*12 + ['2015']*12

grafico = pd.DataFrame({
    "Mês": meses,
    "Decolagens": ano_total,
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
            range_y = [80000, 100000], 
            title = 'Total de decolagens por mês'
            )

# ---------------------------------------- Mostrando gráfico de barras ----------------------------------------
print('Mostrando gráfico...') # Feedback
fig.show()