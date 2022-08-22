# ----------------------------------------- Importando bibliotecas -----------------------------------------
import pandas as pd
import plotly.express as px
import tabela_utils


# ------------------------------------------- Funções Específicas -------------------------------------------
def faztudo(tabela : pd.DataFrame):
    tabela = tabela_utils.filtrar_colunas(tabela, ['DECOLAGENS'])
    tabela = (tabela['DECOLAGENS'].to_list())
    return tabela


# ---------------------------------------------- Lendo dataset ----------------------------------------------
print('Lendo dataset...') # Feedback
dados = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep = ';', encoding = 'latin') # Encoding resolve problema da acentuação


# --------------------------------------- Manipulando dados necessarios---------------------------------------
print('Filtrando colunas...') # Feedback
colunas_filtradas = tabela_utils.filtrar_colunas(dados, ['ANO', 'MÊS', 'AEROPORTO DE ORIGEM (PAÍS)', 'DECOLAGENS'])

print('Retirando nulos...') # Feedback
dados_sem_nulos = tabela_utils.retirar_nulos(colunas_filtradas)

print('Filtrando anos...') # Feedback
dados_anos = tabela_utils.filtrar_linhas(dados_sem_nulos, 'ANO', ['2013', '2014'])

print('Filtrando mês...') # Feedback
mes_6 = tabela_utils.filtrar_linhas(dados_anos, 'MÊS', ['6'])

print('Filtrando países...') # Feedback
dados_paises = tabela_utils.filtrar_linhas(mes_6, 'AEROPORTO DE ORIGEM (PAÍS)', ['ESTADOS UNIDOS DA AMÉRICA', 'MÉXICO', 'ARGENTINA', 'CHILE', 'EMIRADOS ÁRABES UNIDOS'] )

print('Filtrando o ano de 2013 e somando...') # Feedback
dados_2013 = tabela_utils.filtrar_linhas(dados_paises, 'ANO', ['2013'])
soma_2013 = tabela_utils.soma_por_categoria(dados_2013, 'AEROPORTO DE ORIGEM (PAÍS)', 'DECOLAGENS')

print('Filtrando o ano de 2014 e somando...') # Feedback
dados_2014 = tabela_utils.filtrar_linhas(dados_paises, 'ANO', ['2014'])
soma_2014 = tabela_utils.soma_por_categoria(dados_2014, 'AEROPORTO DE ORIGEM (PAÍS)', 'DECOLAGENS')

print('Passando dataframes pelo faztudo...') # Feedback
ano_2013 = faztudo(soma_2013)
ano_2014 = faztudo(soma_2014)


# --------------------------------------------- Criando Dataframe ---------------------------------------------
decolagens = ano_2013 + ano_2014
aeroporto = ['ESTADOS UNIDOS DA AMÉRICA', 'MÉXICO', 'ARGENTINA', 'CHILE', 'EMIRADOS ÁRABES UNIDOS', 'ESTADOS UNIDOS DA AMÉRICA', 'ARGENTINA', 'CHILE', 'MÉXICO', 'EMIRADOS ÁRABES UNIDOS']
anos = ['2013']*5 + ['2014']*5

grafico = pd.DataFrame({
    "Países": aeroporto,
    "Decolagens": decolagens,
    "Ano": anos
})


# ----------------------------------------- Criando gráfico de barras -----------------------------------------
print('Produzindo gráfico...') # Feedback
fig = px.histogram(grafico, 
                    x = "Países", 
                    y = "Decolagens",
                    color = 'Ano', 
                    color_discrete_sequence = px.colors.qualitative.Prism,
                    barmode = 'group',
                    histfunc = 'avg',
                    title = 'Voos por país durante a copa',
                    template ='plotly_dark'
                    )


# ---------------------------------------- Mostrando gráfico de barras ----------------------------------------
print('Mostrando gráfico...') # Feedback
fig.show()