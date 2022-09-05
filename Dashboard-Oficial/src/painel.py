# ----------------------------------------- Importando bibliotecas -----------------------------------------
from dash import Dash, html, dcc, Output, Input

from barras_data_pico import grafico_barras_data_pico
from barras_paises_origem import grafico_barras_paises_origem
from mapa import grafico_mapa
from pizza_preferencia_empresa import grafico_pizza_preferencia_empresa
from pizza_tipo_carga import cria_grafico_pizza_tipo_carga


# ---------------------------------------------- Criando dash ----------------------------------------------
app = Dash(__name__)


# ---------------------------------- Definindo constantes de customização ----------------------------------
cores_texto = {
    'fundo_texto': '#111111',
    'texto': '#7FDBFF'
}


# --------------------------------------------- Criando layout ---------------------------------------------
app.layout = html.Div([

    # -------------------------- Titulos --------------------------
    html.Div(
        style = {'backgroundColor': cores_texto['fundo_texto']},
        children = [
            html.H1(
                children = 'Trafego Aéreo no Brasil',
                style = {
                    'textAlign': 'center',
                   ' fontSize': '150%',
                    'fontFamily': ['Brush Script MT', 'cursive'],
                    'color': cores_texto['texto']
                }
            ),

            html.H2(
                children = 'Os 5 graficos:',
                style = {
                    'textAlign': 'center',
                    'fontFamily': ['Copperplate', 'Papyrus', 'fantasy'],
                    'color': cores_texto['texto']
                }
            )
        ]
    ),

    # --------------------- Primeiro Grafico ---------------------
    html.Div(
        style = {
            'width': '100%',
            'padding': '0 20'
        },
        children = [
            dcc.Graph(
                id = 'grafico_mapa',
                figure = grafico_mapa
            )
        ]
    ),
    
    # --------------------- Segundo Grafico ---------------------
    html.Div(
        style = {
            'width': '100%', 
            'padding': '0 20'
        },
        children = [
            dcc.Graph(
                id='grafico_barras_paises_origem',
                figure = grafico_barras_paises_origem
            )
        ]
    ),

    # --------------------- Terceiro Grafico ---------------------
    html.Div(
        style = {
            'width': '100%', 
            'padding': '0 20'
        },
        children = [
            dcc.Graph(
                id = 'grafico_barras_data_pico',
                figure = grafico_barras_data_pico
            )
        ]
    ),
    
    # --------------------- Quarto Grafico ---------------------
    html.Div(
        style = {
            'width': '100%', 
            'padding': '0 20'
        },
        children = [
            dcc.Graph(
                id = 'grafico_pizza_preferencia_empresa',
                figure = grafico_pizza_preferencia_empresa
            )
        ]
    ),

    # --------------------- Quinto Grafico ---------------------
    html.Div(
        style = {
            'backgroundColor': cores_texto['fundo_texto'],
            'width': '100%', 
            'padding': '0 20'
        },
        children = [
            html.H2(
                children = 'Percentual de peso transportado pelos avioes no Brasil em 20XX',
                id = 'titulo_grafico_pizza_tipo_carga',
                style = {
                    'textAlign': 'center',
                    'fontFamily': ['Copperplate', 'Papyrus', 'fantasy'],
                    'color': cores_texto['texto']
                }
            ),
            html.Label(
                children = 'Selecione os anos que deseja analizar',
                style = {
                    'fontFamily': ['Brush Script MT', 'cursive'],
                    'color': cores_texto['texto'],
                }
            ),
            dcc.Dropdown(
                id = 'filtro_ano',
                options = ['2013', '2014', '2015'], 
                value = ['2013', '2014', '2015'], 
                multi = True,
                style = {
                    'fontFamily': ['Brush Script MT', 'cursive'],
                    'color': cores_texto['texto'],
                }
            ),
            dcc.Graph(
                id = 'grafico_pizza_tipo_carga',
                figure = cria_grafico_pizza_tipo_carga(['2013', '2014', '2015'])
            )
        ]
    )
])


# -------------------------------------- Interatividade Quinto Grafico --------------------------------------
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
        anos = str(", ".join(value[:-1])) + ' e ' + str(value[-1])
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


# ------------------------------------------ Colocando dash no ar ------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)