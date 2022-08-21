# ----------------------------------------- Importando bibliotecas -----------------------------------------
import pandas as pd
import plotly.express as px
import tabela_utils


# ------------------------------------------- Funções Específicas -------------------------------------------
def tirazero(tabela: pd.DataFrame):  # TODO remover ja que é inutil
    tabela = tabela.to_dict()
    apagar=[]
    for cabecalho in tabela:
        linhas = tabela[cabecalho]
        for index in linhas:
            if linhas[index] == 0:
                apagar.append(index)
    for linha in apagar:
        for coluna in tabela:
            tabela[coluna].pop(linha)
    return pd.DataFrame(tabela)


# ---------------------------------------------- Lendo dataset ----------------------------------------------
print('Lendo dataset...') # Feedback
dados = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep = ';', encoding = 'latin') # Encoding resolve problema da acentuação


# --------------------------------------- Manipulando dados necessarios---------------------------------------
print('Filtrando os dados...') # Feedback
dados = tabela_utils.filtrar(dados, ['ANO', 'EMPRESA (NOME)', 'PASSAGEIROS PAGOS'])

print('Retirando os nulos...') # Feedback
dados = tabela_utils.retirar_nulos(dados)

print('Somando por categoria...') # Feedback
dados = tabela_utils.soma_por_categoria(dados, 'EMPRESA (NOME)', 'PASSAGEIROS PAGOS')

dados = tirazero(dados) # TODO remover ja que é inutil

print('Separando empresas com contribuição ínfima...') # Feedback
dados_1 = tabela_utils.outros(dados, 'PASSAGEIROS PAGOS', 1500000)
dados_2 = tabela_utils.outros2(dados, 'PASSAGEIROS PAGOS', 1500000) # TODO pq isso esta sendo feito se df2 nao é usada em lugar nenhum
print(dados)


# ----------------------------------------- Criando gráfico de pizza -----------------------------------------
print('Produzindo gráfico...') # Feedback
setores = px.pie(dados_1, 
                names = 'EMPRESA (NOME)',
                values = 'PASSAGEIROS PAGOS', 
                color_discrete_sequence = px.colors.qualitative.Prism, 
                template = 'plotly_dark'
                )


# ---------------------------------------- Mostrando gráfico de pizza ----------------------------------------
print('Mostrando gráfico...') # Feedback
setores.show()