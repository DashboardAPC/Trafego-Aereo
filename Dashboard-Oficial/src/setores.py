import tabela_utils
import pandas as pd
import plotly.express as px

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

def outros(tabela: pd.DataFrame, cabeçalho_selecionado: str, alvo: int) -> pd.DataFrame:
    tabela = tabela.to_dict()
    fatiador = []
    linha = tabela[cabeçalho_selecionado]
    for id in linha:
        if linha[id] < alvo:
            fatiador.append(id)
    for linha in fatiador:
        for corte in tabela:
            tabela[corte].pop(linha)
    return pd.DataFrame(tabela)

def outros2(tabela: pd.DataFrame, cabeçalho_selecionado: str, alvo: int) -> pd.DataFrame:
    tabela = tabela.to_dict()
    fatiador = []
    linha = tabela[cabeçalho_selecionado]
    for id in linha:
        if linha[id] > alvo:
            fatiador.append(id)
    for linha in fatiador:
        for corte in tabela:
            tabela[corte].pop(linha)
    return pd.DataFrame(tabela)

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
df=tabela_utils.filtrar(df,['ANO', 'EMPRESA (NOME)','PASSAGEIROS PAGOS'])
df=tabela_utils.retirar_nulos(df)
df = tabela_utils.soma_por_categoria(df, 'EMPRESA (NOME)', 'PASSAGEIROS PAGOS')
df = tirazero(df)

df1 = outros(df, 'PASSAGEIROS PAGOS', 1500000)
df2 = outros2(df, 'PASSAGEIROS PAGOS', 1500000)
print(df)

setores=px.pie(df1, names='EMPRESA (NOME)',values='PASSAGEIROS PAGOS', color_discrete_sequence=px.colors.qualitative.Prism, template='plotly_dark')
setores.show()
