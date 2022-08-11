import pandas as pd
import math

def max(tabela: pd.DataFrame)

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
        
            


def filtrar(tabela: pd.DataFrame, filtros: list) -> pd.DataFrame: 
    """Função feita para filtrar colunas em Dataframes

    Args:
        tabela (pd.DataFrame): A tabela que será filtrada
        filtros (list): Lista de colunas que serão mantidas

    Returns:
        pd.DataFrame: Dataframe com as colunas filtradas
    """
    tabela = tabela.to_dict()
    colunas_a_remover=[]

    #Checar quais colunas não estão no filtro
    for coluna in tabela:
        if not coluna in filtros:
            colunas_a_remover.append(coluna)
        
    #Remover todas as colunas com o nome na lista
    for coluna in colunas_a_remover:
        tabela.pop(coluna)
    
    #Transformar tabela em um dataframe novamente
    return pd.DataFrame(tabela)


def retirar_nulos(tabela: pd.DataFrame) -> pd.DataFrame:
    """Retira todas as linhas que contenham qualquer valor NaN de uma tabela

    Args:
        tabela (pd.DataFrame): A tabela a ser operada

    Returns:
        pd.DataFrame: Uma tabela com os valores nulos retirados
    """
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