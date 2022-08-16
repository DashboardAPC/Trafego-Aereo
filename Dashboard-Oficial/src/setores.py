import tabela_utils
import pandas as pd
import plotly.express as px

def outros(tabela: pd.Dataframe):
    tabela= (tabela: pd.DataFrame):
    

def tirazero(tabela: pd.DataFrame):
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

df=pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv',sep=';', encoding='latin')
df=tabela_utils.filtrar(df,['EMPRESA (NOME)','PASSAGEIROS PAGOS'])
df=tabela_utils.retirar_nulos(df)
df = tabela_utils.soma_por_categoria(df, 'EMPRESA (NOME)', 'PASSAGEIROS PAGOS')
df = tirazero(df)
print(df)
setores=px.pie(df, names='EMPRESA (NOME)',values='PASSAGEIROS PAGOS')
setores.show()
