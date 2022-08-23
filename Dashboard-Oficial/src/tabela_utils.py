# ----------------------------------------- Importando bibliotecas -----------------------------------------
import pandas as pd
import math

# ------------------------------------------------ Funções ------------------------------------------------
def filtrar_colunas(tabela: pd.DataFrame, filtros: list) -> pd.DataFrame: 
    """Filtra colunas mantendo apenas as especificadas no argumento 'filtros'

    Args:
        tabela (pd.DataFrame): A tabela que será filtrada
        filtros (list): Lista de colunas que serão mantidas

    Returns:
        pd.DataFrame: Dataframe com as colunas filtradas
    """
    linhas = tabela.values.tolist()
    cabecalhos = tabela.columns.to_list()
    indexes = []
    resultado = []

    cabecalhos_filtrados = []
    for cabecalho in cabecalhos:
        if cabecalho in filtros:
            indexes.append(cabecalhos.index(cabecalho))
            cabecalhos_filtrados.append(cabecalho)
    
    linha_filtrada = []
    for linha in linhas:
        linha_filtrada = []
        for index in indexes:
            linha_filtrada.append(linha[index])
        resultado.append(linha_filtrada)

    return pd.DataFrame(resultado, columns = cabecalhos_filtrados)



def filtrar_linhas(tabela: pd.DataFrame, coluna: str, filtro: list) -> pd.DataFrame:
    """Filtra linhas mantendo apenas as especificadas no argumento 'filtro'
    
    Args:
        tabela (pd.DataFrame): Tabela a ser operada
        coluna (str): Coluna que contem os valores do filtro
        filtro (list): Linhas que devem permanecer na tabela
    Returns:
        pd.DataFrame: Tabela apenas com linhas colocadas no filtro
    """
    tabela = tabela.to_dict()
    linhas = tabela[coluna]
    linhas_a_apagar = []

    for index in linhas:
        valor = linhas[index]
        if not str(valor) in filtro:
            linhas_a_apagar.append(index)
    
    for linha in linhas_a_apagar:
        for cabecalho in tabela:
            tabela[cabecalho].pop(linha)
    
    return pd.DataFrame(tabela)



def retirar_nulos(tabela: pd.DataFrame) -> pd.DataFrame:
    """Retira todas as linhas da tabela que contenham um valor NaN 

    Args:
        tabela (pd.DataFrame): A tabela a ser operada
    Returns:
        pd.DataFrame: Uma tabela com os valores NaN retirados
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
    
    return pd.DataFrame(linhas_resultado, columns = cabecalhos)



def soma_por_categoria(tabela: pd.DataFrame, categoria: str, soma: str) -> pd.DataFrame:
    """
    Efetua a operação de soma para cada categoria diferente em uma certa coluna

    Args:
        tabela (pd.DataFrame): tabela de entrada
        categoria (str): coluna onde estarão as categorias
        soma (str): coluna onde serão somados os valores

    Returns:
        pd.DataFrame: tabela com os valores agregados
    """
    linhas = tabela.values.tolist()
    cabecalhos = tabela.columns.to_list()

    #Pegar a posição do cabecalho de categoria e de soma
    index_cat = cabecalhos.index(categoria)
    index_sum = cabecalhos.index(soma)

    #Criar duas listas representando os valores das duas colunas
    #na tabela resultante(linhas com as somas, linhas com as categorias)
    linhas_categoria = []
    linhas_somas = []

    for linha in linhas:
        categoria_atual = linha[index_cat]
        valor_atual = linha[index_sum]
        if categoria_atual not in linhas_categoria:
            #Se a categoria não estiver registrada
            #simplesmente adicionar ela no final da tabela
            linhas_categoria.append(categoria_atual)
            linhas_somas.append(valor_atual)
            #Pular o loop atual para que não seja adicionado o valor duas vezes
            continue
        # pegar a posição da linha com a categoria atual na tabela de resultado
        linha_atual = linhas_categoria.index(categoria_atual)
        # somar esse valor na lista com as linhas contendo as somas 
        linhas_somas[linha_atual]+=valor_atual

    #Montar a tabela através de um dicionário >:(
    resultado={
        categoria:linhas_categoria,
        soma:linhas_somas
    }

    #Aqui como o dicionário representado a tabela final fica após todas as operações
    #resultado = {
    # 'AEROPORTO DE DESTINO (UF)': ['RJ', 'SP', 'DF', 'MG', 'AM', 'PE', 'BA', 'GO', 'PR', 'RS', 'CE', 'RN', 'AL', 'SC', 
    # 'PA', 'MA', 'ES', 'MT', 'MS', 'RO', 'PI', 'TO', 'SE', 'PB', 'RR', 'AC', 'AP'],
    #  'DECOLAGENS': [356716.0, 909099.0, 233553.0, 229449.0, 72948.0, 102120.0, 168258.0,
    #  53200.0, 173128.0, 120609.0, 84549.0, 30719.0, 23870.0, 92419.0, 107787.0, 34581.0, 48608.0,
    #  61407.0, 31413.0, 20458.0, 18008.0, 17019.0, 19312.0, 18772.0, 4372.0, 6850.0, 10188.0]
    # }

    return pd.DataFrame(resultado)



def soma_generica_colunas(tabela: pd.DataFrame) -> pd.DataFrame:
    """Soma todos os valores de cada coluna separadamente, só aceita valores somaveis
    
    Args:
        tabela (pd.DataFrame): Tabela a ser operada
    Returns:
        pd.DataFrame: Tabela com 2 linhas, cabeçalho + colunas somadas
    """
    tabela_cabecalho = tabela.columns.tolist() # Transformando o cabeçalho do dataframe pra lista
    tabela_valores = tabela.values.tolist() # Transformando os valores do dataframe pra lista
    lista_somas = [] # Lista onde serão armazenadas as respostas da soma de cada coluna
    
    for coluna in range(len(tabela_cabecalho)): # Fazendo uma repetição pra cada coluna
        soma_coluna = 0
        for linha in range(len(tabela_valores)): # Fazendo uma repetição pra cada linha da coluna atual
            soma_coluna += tabela_valores[linha][coluna]    
        lista_somas.append(soma_coluna)
    return pd.DataFrame([lista_somas], columns = tabela_cabecalho) 



def transposicao_eixos(tabela: pd.DataFrame, novo_cabecalho: list) -> pd.DataFrame:
    """Faz a transposição de uma matriz, as linhas viram colunas e as colunas linhas. Obs.: max 2 linhas de entrada

    Args:
        tabela (pd.DataFrame): Tabela a ser transposta
        novo_cabecalho: (list): Cabeçalho que sera colocado na tabela nova
    Returns:
        pd.DataFrame: Dataframe com os colunas e linhas transpostas
    """
    antigo_cabecalho = tabela.columns.tolist() # Transformando o cabeçalho do dataframe pra lista
    antigo_valores = tabela.values.tolist() # Transformando os valores do dataframe pra lista
    lista_intermediaria = [antigo_cabecalho] + antigo_valores
    novo_valores = []

    for linha in range(len(lista_intermediaria[0])):
        nova_linha = []
        for coluna in range(len(lista_intermediaria)):
            nova_linha.append(lista_intermediaria[coluna][linha])
        novo_valores.append(nova_linha)

    return pd.DataFrame(novo_valores, columns = novo_cabecalho) 



def maximo(tabela: pd.DataFrame, cabecalho_max: str) -> float:
    """Calcula o valor máximo de uma coluna

    Args:
        tabela (pd.DataFrame): Tabela a ser operada
        cabecalho_max (str): coluna a ser operada
    Returns:
        float: Valor máximo dentro da coluna
    """
    linhas = tabela.values.tolist()
    cabecalhos = tabela.columns.to_list()
    maximo = 0
    
    for linha in linhas:
        atual = linha[cabecalhos.index(cabecalho_max)]
        if atual > maximo:
            maximo = atual
    
    return maximo



def remover_insignificantes(tabela: pd.DataFrame, cabeçalho_selecionado: str, alvo: int) -> pd.DataFrame:
    """Mantem na tabela apenas valores acima do limite estabelecido pelo parametro 'alvo'

    Args:
        tabela (pd.DataFrame): Tabela a ser operada
        cabeçalho_selecionado (str): Coluna que contem os valores a serem analizados
        alvo (int): Valor minimo que sera mantido na tabela
    Returns:
        pd.DataFrame: Tabela com apenas linhas com valores superiores ao alvo
    """
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