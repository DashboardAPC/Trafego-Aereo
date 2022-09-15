# ----------------------------------------- Importando bibliotecas -----------------------------------------
import pandas as pd
import plotly.express as px
import tabela_utils


# ---------------------------------------------- Lendo dataset ----------------------------------------------
print('4 - Lendo dataset...') # Feedback
csv = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep = ';', encoding = 'latin') # Encoding resolve problema da acentuação

def criar_setores(ano='2013',minimo=1500000):
    dados = tabela_utils.filtrar_linhas(csv,'ANO',[ano])
    # --------------------------------------- Manipulando dados necessarios---------------------------------------
    print('4 - Filtrando os dados...') # Feedback
    dados = tabela_utils.filtrar_colunas(dados, ['ANO', 'EMPRESA (NOME)', 'PASSAGEIROS PAGOS'])

    print('4 - Retirando os nulos...') # Feedback
    dados = tabela_utils.retirar_nulos(dados)

    print('4 - Somando por categoria...') # Feedback
    dados = tabela_utils.soma_por_categoria(dados, 'EMPRESA (NOME)', 'PASSAGEIROS PAGOS')

    print('4 - Separando empresas com contribuição ínfima...') # Feedback
    dados = tabela_utils.remover_insignificantes(dados, 'PASSAGEIROS PAGOS', minimo)


    # ----------------------------------------- Criando gráfico de pizza -----------------------------------------
    print('4 - Produzindo gráfico...') # Feedback
    grafico_pizza_preferencia_empresa = px.pie(dados, 
                    names = 'EMPRESA (NOME)',
                    values = 'PASSAGEIROS PAGOS', 
                    color_discrete_sequence = px.colors.qualitative.Prism, 
                    template = 'plotly_dark',
                    title = 'Empresas aéreas preferidas pelo consumidor'
                    )
    return grafico_pizza_preferencia_empresa
criar_setores().show()