def filtrar(tabela: pd.DataFrame, filtros: list) -> pd.DataFrame: 
    """Função feita para filtrar colunas em Dataframes

    Args:
        tabela (pd.DataFrame): A tabela que será filtrada
        filtros (list): Lista de colunas que serão mantidas

    Returns:
        pd.DataFrame: Dataframe com as colunas filtradas
    """
    resultado={}
    tabela = tabela.to_dict()
    for cabecalho in  tabela:
        if cabecalho in filtros:
            resultado[cabecalho]=tabela[cabecalho]
    resultado_pd = pd.DataFrame(resultado)
    return resultado_pd