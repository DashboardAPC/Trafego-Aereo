# ----------------------------------------- Importando bibliotecas -----------------------------------------
import pandas as pd
import plotly.express as px
import tabela_utils


def cria_grafico_pizza_tipo_carga(anos):
        # ------------------------------------------ Lendo dataset ------------------------------------------
        print('Lendo dataset...') # Feedback
        dados = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep = ';', encoding = 'latin') # Encoding resolve problema da acentuação


        # ----------------------------------- Manipulando dados necessários-----------------------------------
        print('Filtrando dados colunas necessarias do dataset...') # Feedback
        dados = tabela_utils.filtrar_colunas(dados, ['ANO', 'CARGA PAGA (KG)', 'CARGA GRÁTIS (KG)', 'CORREIO (KG)', 'BAGAGEM (KG)'])

        print('Removendo valores invalidos...') # Feedback
        dados = tabela_utils.retirar_nulos(dados)

        print('Separando anos...') # Feedback
        peso_nos_anos = tabela_utils.filtrar_linhas(dados, 'ANO', anos)

        print('Filtrando fora coluna ano...') # Feedback
        peso_nos_anos = tabela_utils.filtrar_colunas(peso_nos_anos, ['CARGA PAGA (KG)', 'CARGA GRÁTIS (KG)', 'CORREIO (KG)', 'BAGAGEM (KG)'])

        print('Somando tudo...') # Feedback
        peso_nos_anos = tabela_utils.soma_generica_colunas(peso_nos_anos)

        print('Transpondo tabelas...') # Feedback
        peso_nos_anos = tabela_utils.transposicao_eixos(peso_nos_anos, ['Tipo de peso', 'KG'])


        # ------------------------------------ Criando gráfico de pizza ------------------------------------
        print('Produzindo gráfico...') # Feedback
        grafico_pizza_tipo_carga = px.pie(peso_nos_anos,
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
                marker = dict(line = dict(color = 'rgb(17, 17, 17)', width = 3))
                )
        

        # ---------------------------------- Retornando gráfico de pizza ----------------------------------
        return grafico_pizza_tipo_carga