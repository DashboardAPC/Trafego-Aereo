# ----------------------------------------- Importando bibliotecas -----------------------------------------
import pandas as pd
import plotly.express as px
import tabela_utils

def cria_grafico_barras_paises_origem(anos, mes, paises):

    # ---------------------------------------------- Lendo dataset ----------------------------------------------
    print('2 - Lendo dataset...') # Feedback
    dados = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep = ';', encoding = 'latin') # Encoding resolve problema da acentuação


    # --------------------------------------- Manipulando dados necessarios---------------------------------------
    print('2 - Filtrando colunas...') # Feedback
    colunas_filtradas = tabela_utils.filtrar_colunas(dados, ['ANO', 'MÊS', 'AEROPORTO DE ORIGEM (PAÍS)', 'DECOLAGENS'])

    print('2 - Retirando nulos...') # Feedback
    dados_sem_nulos = tabela_utils.retirar_nulos(colunas_filtradas)

    print('2 - Filtrando anos...') # Feedback
    dados_anos = tabela_utils.filtrar_linhas(dados_sem_nulos, 'ANO', anos)

    print('2 - Filtrando mês...') # Feedback
    mes_6 = tabela_utils.filtrar_linhas(dados_anos, 'MÊS', mes)
    
    print('2 - Filtrando países...') # Feedback
    dados_paises = tabela_utils.filtrar_linhas(mes_6, 'AEROPORTO DE ORIGEM (PAÍS)', paises )

    soma_2013 = tabela_utils.soma_por_categoria(dados_paises, 'AEROPORTO DE ORIGEM (PAÍS)', 'DECOLAGENS')

    # ----------------------------------------- Criando gráfico de barras -----------------------------------------
    print('2 - Produzindo gráfico...') # Feedback
    grafico_barras_paises_origem = px.histogram(soma_2013, 
                        y = "DECOLAGENS", 
                        x = "AEROPORTO DE ORIGEM (PAÍS)",
                        color_discrete_sequence = px.colors.qualitative.Prism,
                        barmode = 'group',
                        title = 'Países de origem dos voos no mês de Junho em 2013 e 2014',
                        template ='plotly_dark'
                        )
    return grafico_barras_paises_origem

cria_grafico_barras_paises_origem