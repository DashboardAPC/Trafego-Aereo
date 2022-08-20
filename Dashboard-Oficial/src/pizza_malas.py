# ---------------------------- Grafico de Pizza sobre peso carregado pelos avioes ----------------------------
import pandas as pd
import plotly.express as  px
import tabela_utils

# ---------------------------------------------- Funcoes uteis ----------------------------------------------
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


# ---------------------------------------------- Lendo dataset ----------------------------------------------
print('Lendo dataset...') # Feedback
voos = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep=';', encoding='latin') #Encoding sendo usado para evitar problemas com acentuacao


# --------------------------------------- Manipulando dados necessarios---------------------------------------
print('Filtrando dados colunas necessarias do dataset...') # Feedback
tabela_de_pesos = tabela_utils.filtrar(voos, ['ANO','CARGA PAGA (KG)','CARGA GRÁTIS (KG)','CORREIO (KG)','BAGAGEM (KG)'])

print('Removendo valores invalidos...') # Feedback
tabela_de_pesos = tabela_utils.retirar_nulos(tabela_de_pesos)

print('Separando anos...') # Feedback
peso_2013 = tabela_utils.filtrar_linha(tabela_de_pesos, 'ANO', ['2014','2015'])
peso_2014 = tabela_utils.filtrar_linha(tabela_de_pesos, 'ANO', ['2013','2015'])
peso_2015 = tabela_utils.filtrar_linha(tabela_de_pesos, 'ANO', ['2013','2014'])

print('Filtrando fora coluna ano...') # Feedback
peso_2013_pre_soma = tabela_utils.filtrar(peso_2013, ['CARGA PAGA (KG)','CARGA GRÁTIS (KG)','CORREIO (KG)','BAGAGEM (KG)'])
peso_2014_pre_soma = tabela_utils.filtrar(peso_2014, ['CARGA PAGA (KG)','CARGA GRÁTIS (KG)','CORREIO (KG)','BAGAGEM (KG)'])
peso_2015_pre_soma = tabela_utils.filtrar(peso_2015, ['CARGA PAGA (KG)','CARGA GRÁTIS (KG)','CORREIO (KG)','BAGAGEM (KG)'])

print('Somando tudo...') # Feedback
peso_2013_somado = soma_generica_colunas(peso_2013_pre_soma)
peso_2014_somado = soma_generica_colunas(peso_2014_pre_soma)
peso_2015_somado = soma_generica_colunas(peso_2015_pre_soma)

# TODO transformar todas as funcoes a cima em uma unica que chama as outras

# -------------------------------- Futuro dropdown do Dashboard (Substituir) --------------------------------
print('De que ano gostaria de ver o grafico pizza? Digite 2013, 2014 ou 2015')
# TODO todo esse loop poderia ser substituido por uma funcao mais flexivel que suporte um caso de nao ser so 3 anos talvez adaptando o dataset peso_XXXX pra manter a informacao do ano.

while True:
    ano_desejado = input()
    if ano_desejado == '2013':
        tabela_entrada_pizza = peso_2013_somado
        break
    elif ano_desejado == '2014':
        tabela_entrada_pizza = peso_2014_somado
        break
    elif ano_desejado == '2015':
        tabela_entrada_pizza = peso_2015_somado
        break
    else:
        print('Valor incorreto. Por favor digite 2013, 2014 ou 2015')



# ----------------------------------- TODO: Cai na fake news do caio -----------------------------------
tabela_entrada_pizza = tabela_entrada_pizza.transpose()
# O .transpose provavelmente nao é permitido. Mas sehundo o Mago de APC nao é necesssario fazer a mudanca de eixos. Eu nao consegui plotar a figura sem mudar os eixos entao esse cara vai ficar aqui ate eu a) fazer uma funcao pra substituir ou b) fazer funcionar sem a transposicao de eixos

# ----------------------------------- Mostrando tabela do grafico de pizza -----------------------------------
# print(tabela_entrada_pizza)


# ----------------------------------------- Criando gráfico de pizza -----------------------------------------
pizza = px.pie(tabela_entrada_pizza,
        values = 1,
        names = 0,
        width = 960,
        height = 540,
        hole = .4,
        template = 'simple_white',
        title = 'Percentual de peso transportado pelos avioes no Brasil de de 2013 à 2015'
        )


# ---------------------------------- Umas frescura pra uma pizza bunitinha ----------------------------------
pizza.update_traces(textinfo = "label+percent", 
        insidetextfont=dict(color="white")
        )


# ---------------------------------------- Mostrando gráfico de pizza ----------------------------------------
pizza.show()