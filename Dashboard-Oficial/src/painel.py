# ----------------------------------------- Importando bibliotecas -----------------------------------------
from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc

from barras_data_pico import grafico_barras_data_pico
from barras_paises_origem import grafico_barras_paises_origem
from mapa import criar_mapa, criar_lista_dropdowns, dados_validos
from pizza_preferencia_empresa import grafico_pizza_preferencia_empresa
from pizza_tipo_carga import cria_grafico_pizza_tipo_carga


# ---------------------------------------------- Criando dash ----------------------------------------------
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])


# --------------------------------------- Criando Bloco de Títulos ---------------------------------------
bloco_titulo = [
    html.H1(
        children = 'Trafego Aéreo no Brasil',
        style = {
            'textAlign': 'center',
            'fontSize': '150%',
            'fontFamily': ['Brush Script MT', 'cursive']
        }
    ),

    html.H2(
        children = 'Os 5 graficos:',
        style = {
            'textAlign': 'center',
            'fontFamily': ['Copperplate', 'Papyrus', 'fantasy']
        }
    )
]

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
        id = 'grafico-mapa',style={'height':'100vh'}
    )
]

controles = dbc.Card([
    html.Div([
        dbc.Label('Escolha um ano'),
        dbc.RadioItems(
            options=[
                {'label':'2013','value':'2013'},
                {'label':'2014','value':'2014'},
                {'label':'2015','value':'2015'},
            ],
            value='2013',
            id='escolha-ano-mapa',
            inline=True
            )
        ]
    ),
    html.Div([  
        dbc.Label('Digite uma Unidade Federativa e pressione enter'),
        dbc.Input(value='DF',type='text',id='escolha-estado-mapa', debounce=True)
        ]
    )
], body=True
)

# --------------------------------------- Criando Bloco do Gráfico 4 ---------------------------------------
bloco_g4 = [
    dcc.Graph(
        id = 'grafico_pizza_preferencia_empresa',
        figure = grafico_pizza_preferencia_empresa
    )
]

# --------------------------------------- Criando Bloco do Gráfico 5 ---------------------------------------
bloco_g5 = [
    html.H5(
        children = 'Percentual de peso transportado pelos avioes no Brasil em 20XX',
        id = 'titulo_grafico_pizza_tipo_carga',
        style = {
            'textAlign': 'center',
            'fontFamily': ['Copperplate', 'Papyrus', 'fantasy'],
            'backgroundColor': '#111111'
        }
    ),

    html.Label(
        children = 'Selecione os anos que deseja analizar',
        style = {
            'fontFamily': ['Brush Script MT', 'cursive'],
            'backgroundColor': '#111111'
        }
    ),

    dcc.Dropdown(
        id = 'filtro_ano',
        options = ['2013', '2014', '2015'], 
        value = ['2013', '2014', '2015'], 
        multi = True,
        style = {
            'fontFamily': ['Brush Script MT', 'cursive'],
            'backgroundColor': '#111111'
        }
    ),

    dcc.Graph(
        id = 'grafico_pizza_tipo_carga',
        figure = cria_grafico_pizza_tipo_carga(['2013', '2014', '2015'])
    )
]


# --------------------------------------------- Criando layout ---------------------------------------------
app.layout = dbc.Container([

    dbc.Row(bloco_titulo, style = {'height': '100vh'}),

    dbc.Row([
        dbc.Col([
            dbc.Row(bloco_g1, style = {'height': '50vh'}),
            dbc.Row(bloco_g2, style = {'height': '50vh'})
        ], md=4),
        
        dbc.Col([
            dbc.Row(bloco_g4, style = {'height': '50vh'}),
            dbc.Row(bloco_g5, style = {'height': '50vh'})
        ], md=3),
    ], className='g-0'),

    dbc.Row([
        dbc.Col(controles, md=4, style={'width':'50vh'}),
        dbc.Col(bloco_g3, md=8, style={'width':'50vh'}),
        ], align='center', style = {'height':'100vh', 'width':'100vh'}),

], fluid=True)


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
    anos = [float(item) for item in value] # TODO: Essa adaptacao horrivel pode ser removida se descobrirmos pq filtrar nulos esta transformando os numeros em float
    anos = [str(item) for item in anos]
    if value == []: # No caso especifico do usuario limpar o Dropdown deve mostrar por padrao de todos os anos
        anos = ['2013.0', '2014.0', '2015.0']
    return cria_grafico_pizza_tipo_carga(anos)

@app.callback(
        Output(component_id='grafico-mapa', component_property='figure'),
        Input(component_id='escolha-ano-mapa', component_property='value'),
        Input(component_id='escolha-estado-mapa', component_property='value')
        )
def parametrizar_mapa(ano,estado):
    figure = 0
    if not dados_validos(estado):
        figure = criar_mapa(ano)
    else:
        figure = criar_mapa(ano,estado)
    return figure

@app.callback(
        Output(component_id='escolha-estado-mapa', component_property='invalid'),
        Input(component_id='escolha-estado-mapa', component_property='value')
        )
def entrada_valida(estado):
    resultado=False
    if not dados_validos(estado):
        resultado=True
    return resultado
# ------------------------------------------ Colocando dash no ar ------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
