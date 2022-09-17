# ----------------------------------------- Importando bibliotecas -----------------------------------------
from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc

from barras_data_pico import grafico_barras_data_pico
from barras_paises_origem import grafico_barras_paises_origem
from mapa import grafico_mapa
from pizza_preferencia_empresa import grafico_pizza_preferencia_empresa
from pizza_tipo_carga import cria_grafico_pizza_tipo_carga

# ---------------------------------------------- Estilização ----------------------------------------------
dicionario_estilo_blocos = {
    'height': '100vh', 
    'padding':'5vh',
    'marginTop': 10,
    'marginBottom': 10
    }


# ---------------------------------------------- Criando dash ----------------------------------------------
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])


# --------------------------------------- Criando Bloco de Títulos ---------------------------------------
bloco_titulo = dbc.Card(
    children = [
        html.H1(
            children = 'Trafego Aéreo no Brasil',
            style = {
                'textAlign': 'center',
                'fontSize': '200%',
                # 'fontFamily': ['Brush Script MT', 'cursive']
            }
        ),

        html.H5(
            children = '    Dashborad sobre o Trafego Aéreo no Brasil, desenvolvido pelos estudantes da disciplina de Algoritimos e Programação de Computadores como Trabalho Final', # TODO colocar nomes dos integrantes pra aparecer ao clicar em um botão
            style = {
                'padding':'2vh',
                'fontFamily': ['Copperplate', 'Papyrus', 'fantasy']
            }
        )
],
    style = {
        'height': '40vh', 
        'marginTop': '60vh',
        'marginLeft': 20, 
        'width': '800px',
        'backgroundColor': '#060606',
    }
)


# # --------------------------------------- Criando Barra de Navegação --------------------------------------- TODO WIP
# barra_navegacao = dbc.Nav([
#         dbc.NavItem(dbc.NavLink('ir começo', href = '#')),
#         dbc.NavItem(dbc.NavLink('ir mapa e pizza', href = '#tela_1')),
#         dbc.NavItem(dbc.NavLink('ir barra 1', href = '#tela_2')),
#         dbc.NavItem(dbc.NavLink('ir barra 2', href = '#tela_3')),
#     ],
#     navbar_scroll=True,
#     # vertical = 'md', 
#     pills = True,
# )


# --------------------------------------- Criando Bloco do Gráfico 1 ---------------------------------------
bloco_g1 = [
    dcc.Graph(
        id = 'grafico_barras_data_pico',
        figure = grafico_barras_data_pico
    )
]

# --------------------------------------- Criando Bloco do Gráfico 2 ---------------------------------------
bloco_g2 = [
    dcc.Graph(
        id='grafico_barras_paises_origem',
        figure = grafico_barras_paises_origem
    )    
]

# --------------------------------------- Criando Bloco do Gráfico 3 ---------------------------------------
bloco_g3 = [
    dcc.Graph(
        id = 'grafico_mapa',
        figure = grafico_mapa
    )
]

# --------------------------------------- Criando Bloco do Gráfico 4 ---------------------------------------
bloco_g4 = [
    dcc.Graph(
        id = 'grafico_pizza_preferencia_empresa',
        figure = grafico_pizza_preferencia_empresa
    )
]

# --------------------------------------- Criando Bloco do Gráfico 5 ---------------------------------------
bloco_g5 = dbc.Card(
    children = [
        html.H6(
            children = 'Percentual de peso transportado pelos avioes no Brasil em 20XX',
            id = 'titulo_grafico_pizza_tipo_carga',
            style = {
                'fontSize': '150%',
                'textAlign': 'center',
                'fontFamily': ['Copperplate', 'Papyrus', 'fantasy']
            }
        ),

        html.Label(
            children = 'Selecione os anos que deseja analizar',
            style = {
                'fontFamily': ['Brush Script MT', 'cursive'],
            }
        ),

        dcc.Dropdown(
            id = 'filtro_ano',
            options = ['2013', '2014', '2015'], # TODO como obter anos lendo o dataset
            value = ['2013', '2014', '2015'], 
            multi = True,
            style = {
                'fontFamily': ['Brush Script MT', 'cursive'],
                'backgroundColor': '#111111'
            }
        ),
        
        dcc.Loading(
            type = 'default',
            children = dcc.Graph(
                id = 'grafico_pizza_tipo_carga',
                # figure = cria_grafico_pizza_tipo_carga(['2013', '2014', '2015']),
                )
        )
    ],
    style = {
        'backgroundColor': '#111111',
        'box-shadow' : '5px 5px 10px rgba(255, 146, 4, 0.80)',
        'padding':'0px',
    }
)

# --------------------------------------------- Criando layout ---------------------------------------------
app.layout = dbc.Container([
    # dbc.NavbarSimple( 
    #     children = barra_navegacao,
    #     color = 'primary',
    #     dark = True, 
    #     # fixed = 'top',
    #     sticky = 'top'
    #     ),#TODO WIP

    dbc.Row(
        children = bloco_titulo, 
        style = {
            'height': '100vh', 
            'background': 'url("/assets/fundo_dash.jpg") no-repeat', 
            'background-position': 'center', 
            'background-size': 'cover'
        }
    ),

    dbc.Row([
        dbc.Col([
            dbc.Row(bloco_g1, style = dicionario_estilo_blocos)
        ], md = 5),
        dbc.Col([
            dbc.Row(bloco_g3, style = dicionario_estilo_blocos)
        ], md = 7),
    ], className = 'g-0'),
        
    dbc.Row([
        dbc.Col([
            dbc.Row(bloco_g5, style = dicionario_estilo_blocos),
        ], md = 5),
        dbc.Col([
            dbc.Row(bloco_g4, style = dicionario_estilo_blocos)
        ], md = 7),
    ], className = 'g-0'),

    dbc.Row(bloco_g2, style = dicionario_estilo_blocos, align = 'center', className = 'g-0')

], fluid = True)


# ----------------------------------- Interatividade Bloco do Gráfico 5 -----------------------------------
@app.callback(
    Output(component_id = 'titulo_grafico_pizza_tipo_carga', component_property = 'children'),
    Input(component_id = 'filtro_ano', component_property = 'value')
)
def interatividade_titulo_pizza_tipo_carga(value): # Muda os anos no titulo html do gráfico
    if value == []:
        anos = '2013, 2014 e 2015'
    elif len(value) == 1:
        anos = value[0]
    else:
        value = sorted(value)
        anos = str(', '.join(value[:-1])) + ' e ' + str(value[-1])
    return f'Percentual de peso transportado pelos aviões no Brasil em {anos}'

@app.callback(
    Output(component_id = 'grafico_pizza_tipo_carga', component_property = 'figure'),
    Input(component_id = 'filtro_ano', component_property = 'value')
)
def interatividade_grafico_pizza_tipo_carga(value): # Muda os valores que serão considerados na criação do gráfico
    anos = [float(item) for item in value] # Adaptação é necessaria pra corrigir os valores de entrada que devem ser no formato 2013.0 e não 2013
    anos = [str(item) for item in anos]
    if value == []: # No caso especifico do usuario limpar o Dropdown deve mostrar por padrao todos os anos
        anos = ['2013.0', '2014.0', '2015.0']
    return cria_grafico_pizza_tipo_carga(anos)


# ------------------------------------------ Colocando dash no ar ------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)