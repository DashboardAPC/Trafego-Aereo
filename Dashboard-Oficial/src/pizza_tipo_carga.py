# ----------------------------------------- Importando bibliotecas -----------------------------------------
import pandas as pd
import plotly.express as px
import tabela_utils


def cria_grafico_pizza_tipo_carga(anos):
        # ------------------------------------------ Lendo dataset ------------------------------------------
        print('5 - Lendo dataset...') # Feedback
        dados = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep = ';', encoding = 'latin') # Encoding resolve problema da acentuação


        # ----------------------------------- Manipulando dados necessários-----------------------------------
        print('5 - Filtrando dados colunas necessarias do dataset...') # Feedback
        dados = tabela_utils.filtrar_colunas(dados, ['ANO', 'CARGA PAGA (KG)', 'CARGA GRÁTIS (KG)', 'CORREIO (KG)', 'BAGAGEM (KG)'])

        print('5 - Removendo valores invalidos...') # Feedback
        dados = tabela_utils.retirar_nulos(dados)

        print('5 - Separando anos...') # Feedback
        dados = tabela_utils.filtrar_linhas(dados, 'ANO', anos) # Leva em consideração apenas linhas com 'anos' selecionados no Dropdown pelo usuario

        print('5 - Filtrando fora coluna ano...') # Feedback
        dados = tabela_utils.filtrar_colunas(dados, ['CARGA PAGA (KG)', 'CARGA GRÁTIS (KG)', 'CORREIO (KG)', 'BAGAGEM (KG)'])

        print('5 - Somando tudo...') # Feedback
        dados = tabela_utils.soma_generica_colunas(dados)

        print('5 - Transpondo tabelas...') # Feedback
        dados = tabela_utils.transposicao_eixos(dados, ['Tipo de peso', 'KG'])


        # ------------------------------------ Criando gráfico de pizza ------------------------------------
        print('5 - Produzindo gráfico...') # Feedback
        grafico_pizza_tipo_carga = px.pie(dados,
                        values = 'KG',
                        names = 'Tipo de peso',
                        hole = .4,
                        template = 'plotly_dark',
                        color_discrete_sequence = px.colors.qualitative.Prism
                        )

        grafico_pizza_tipo_carga.update_traces(
                text =  ['CARGA PAGA', 'CARGA GRÁTIS', 'CORREIO', 'BAGAGEM'],
                textinfo = "text + percent", 
                textposition = 'outside',
                hovertemplate = '%{value} Kg',
                marker = dict(line = dict(color = '#111111', width = 3)),
                showlegend = False
                )
        

        # ---------------------------------- Retornando gráfico de pizza ----------------------------------
        return grafico_pizza_tipo_carga