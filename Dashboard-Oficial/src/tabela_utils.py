import pandas as pd
import math

def soma_generica_colunas(tabela: pd.DataFrame) -> pd.DataFrame:
    tabela_cabecalho = tabela.columns.tolist() # Transformando o cabeçalho do dataframe pra lista
    tabela_valores = tabela.values.tolist() # Transformando os valores do dataframe pra lista
    
    lista_somas = [] # Lista onde serão armazenadas as respostas da soma de cada coluna
    for coluna in range(len(tabela_cabecalho)): # Fazendo uma repetição pra cada coluna do cabeçalho
        soma_coluna = 0
        for linha in range(len(tabela_valores)):
            soma_coluna += tabela_valores[linha][coluna]    
        lista_somas.append(soma_coluna)

    resultado = [tabela_cabecalho, lista_somas]
    return pd.DataFrame(resultado)

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

# TODO funcoes outros e outros2 podem ser misturadas com a adicao de um parametro opcional

def filtrar_linha(tabela: pd.DataFrame, coluna: str, filtro:list):
    tabela = tabela.to_dict()
    linhas = tabela[coluna]
    linhas_a_apagar=[]

    for index in linhas:
        valor = linhas[index]
        if not str(valor) in filtro:
            linhas_a_apagar.append(index)
    
    for linha in linhas_a_apagar:
        for cabecalho in tabela:
            tabela[cabecalho].pop(linha)
    
    return pd.DataFrame(tabela)

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

def maximo(tabela: pd.DataFrame, cabecalho_max: str) -> float:
    """Calcula o valor máximo de uma coluna

    Args:
        tabela (pd.DataFrame): Tabela a ser operada
        cabecalho_max (str): coluna a ser operada

    Returns:
        float: Valor máximo dentro da coluna
    """
    linhas=tabela.values.tolist()
    cabecalhos=tabela.columns.to_list()
    maximo = 0
    for linha in linhas:
        atual=linha[cabecalhos.index(cabecalho_max)]
        if atual>maximo:
            maximo=atual
    return maximo


def soma_por_categoria(tabela: pd.DataFrame, cabecalho_categoria: str, cabecalho_a_somar: str) -> pd.DataFrame:
    """Soma os valores de uma coluna para cada valor diferente de outra coluna

    Args:
        tabela (pd.DataFrame): Tabela a ser operada
        cabecalho_categoria (str): Cabeçalho onde estão as categorias
        cabecalho_a_somar (str): Cabeçalho a ser calculada a soma

    Returns:
        pd.DataFrame: Dataframe com os dados calculados
    """
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
        
            


def filtrar(tabela: pd.DataFrame, filtros: list) -> pd.DataFrame: 
    """Função feita para filtrar colunas em Dataframes

    Args:
        tabela (pd.DataFrame): A tabela que será filtrada
        filtros (list): Lista de colunas que serão mantidas

    Returns:
        pd.DataFrame: Dataframe com as colunas filtradas
    """

    linhas = tabela.values.tolist()
    cabecalhos = tabela.columns.to_list()
    indexes=[]
    resultado=[]

    cabecalhos_filtrados=[]
    for cabecalho in cabecalhos:
        if cabecalho in filtros:
            indexes.append(cabecalhos.index(cabecalho))
            cabecalhos_filtrados.append(cabecalho)
    
    linha_filtrada=[]
    for linha in linhas:
        linha_filtrada=[]
        for index in indexes:
            linha_filtrada.append(linha[index])
        resultado.append(linha_filtrada)

    return pd.DataFrame(resultado, columns=cabecalhos_filtrados)


def retirar_nulos(tabela: pd.DataFrame) -> pd.DataFrame:
    """Retira todas as linhas que contenham qualquer valor NaN de uma tabela

    Args:
        tabela (pd.DataFrame): A tabela a ser operada

    Returns:
        pd.DataFrame: Uma tabela com os valores nulos retirados
    """


    linhas = tabela.values.tolist()
    cabecalhos = tabela.columns.to_list()
    linhas_resultado=[]
    invalido = False

    for linha in linhas:
        invalido = False
        for coluna in linha:
            if isinstance(coluna, float):
                if math.isnan(coluna):
                    invalido = True
                    break
        if not invalido:
            linhas_resultado.append(linha)
    
    return pd.DataFrame(linhas_resultado, columns=cabecalhos)