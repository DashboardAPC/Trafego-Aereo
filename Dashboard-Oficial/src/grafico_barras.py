import pandas as pd
import math
import plotly.express as px

#FILTRO FILTRO FILTRO FILTRO
def filtrar(tabela: pd.DataFrame, filtros: list) -> pd.DataFrame: 
    tabela = tabela.to_dict()
    colunas_a_remover=[]
    for coluna in tabela:
        if not coluna in filtros:
            colunas_a_remover.append(coluna)
    for coluna in colunas_a_remover:
        tabela.pop(coluna)
    return pd.DataFrame(tabela)

#RETIRA NULO  RETIRA NULO  RETIRA NULO 
def retirar_nulos(tabela: pd.DataFrame) -> pd.DataFrame:
    linhas_a_retirar=[]
    tabela=tabela.to_dict()
    for cabecalho in tabela:
        coluna=tabela[cabecalho]
        for index in coluna:
            if isinstance(coluna[index], float):
                if math.isnan(coluna[index]) and not index in linhas_a_retirar:
                    linhas_a_retirar.append(index)
    for linha in linhas_a_retirar:
        for cabecalho in tabela:
            tabela[cabecalho].pop(linha)
    return pd.DataFrame(tabela)

#SEPARA E SOMA  SEPARA E SOMA  
def soma_por_categoria(tabela: pd.DataFrame, cabecalho_categoria: str, cabecalho_a_somar: str) -> pd.DataFrame:
    tabela = tabela.to_dict()
    tabela_resultado={cabecalho_categoria:{},cabecalho_a_somar:{}}
    coluna_a_somar = tabela[cabecalho_a_somar]
    coluna_categoria = tabela[cabecalho_categoria]
    soma={}
    for index in coluna_categoria:
        valor_linha = coluna_categoria[index]
        if valor_linha in soma:
            soma[valor_linha]+=coluna_a_somar[index]
        else:
            soma[valor_linha]=coluna_a_somar[index]
    linhas=len(soma)
    i=1
    for categoria in soma:
        tabela_resultado[cabecalho_categoria][i] = categoria
        tabela_resultado[cabecalho_a_somar][i] = soma[categoria]
        i+=1
    return pd.DataFrame(tabela_resultado)

#FATIA FATIA FATIA FATIA
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

dados = pd.read_csv('https://raw.githubusercontent.com/DashboardAPC/DashboardAPC/master/Dashboard-Oficial/data/ANAC20XX-13-14-15.csv', sep=';', encoding='latin')
filtrado = filtrar(dados, ['ANO', 'MÊS', 'DECOLAGENS'])

semnulo = retirar_nulos(filtrado)

ano1 = fatiar(semnulo, 'ANO', 2013)
ano2 = fatiar(semnulo, 'ANO', 2014)
ano3 = fatiar(semnulo, 'ANO', 2015)

ano2013 = soma_por_categoria(ano1, 'MÊS', 'DECOLAGENS')
ano2014 = soma_por_categoria(ano2, 'MÊS', 'DECOLAGENS')
ano2015 = soma_por_categoria(ano3, 'MÊS', 'DECOLAGENS')

ano2013f = filtrar(ano2013, ['DECOLAGENS'])
ano2014f = filtrar(ano2014, ['DECOLAGENS'])
ano2015f = filtrar(ano2015, ['DECOLAGENS'])

ano2013ff = (ano2013f['DECOLAGENS'].to_list())
ano2014ff = (ano2014f['DECOLAGENS'].to_list())
ano2015ff = (ano2015f['DECOLAGENS'].to_list())

anototal = ano2013ff + ano2014ff + ano2015ff

grafico = pd.DataFrame({
    "Mês": ["Janeiro", 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro',"Janeiro", 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro',"Janeiro", 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    "Decolagens": anototal,
    "Ano": ['2013','2013','2013','2013','2013','2013','2013','2013','2013','2013','2013','2013','2014','2014','2014','2014','2014','2014','2014','2014','2014','2014','2014','2014','2015','2015','2015','2015','2015','2015','2015','2015','2015','2015','2015','2015',]
})

fig = px.bar(grafico, x="Mês", y="Decolagens", color="Ano", barmode="group")
fig.show()
