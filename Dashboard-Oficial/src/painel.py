# ----------------------------------------- Importando bibliotecas -----------------------------------------
from dash import Dash, html, dcc, Output, Input, State
import dash_bootstrap_components as dbc

from barras_data_pico import criar_grafico_barras_data_pico
from barras_paises_origem import cria_grafico_barras_paises_origem
from mapa import criar_mapa, dados_validos
from pizza_preferencia_empresa import criar_setores
from pizza_tipo_carga import cria_grafico_pizza_tipo_carga


# ---------------------------------------------- Estilização ----------------------------------------------
dicionario_estilo_blocos = {
    'height': '100vh', 
    'margin': '10px',
    'paddingTop': '10vh',
    'paddingBottom': '10vh'
}
dicionario_estilo_titulos_graficos = {
    'textAlign': 'center',
    'fontFamily': ['Copperplate', 'Papyrus', 'fantasy'],
    'backgroundColor': '#111111'
}

dicionario_estilo_cards = {
        'backgroundColor': '#111111',
        'boxShadow' : '5px 5px 10px rgba(28, 147, 255, 0.80)',
        'padding':'0px'
    }

dicionario_estilo_label = {
    'fontFamily' : ['Brush Script MT', 'cursive'],
    'backgroundColor' : '#111111'       
}
# ---------------------------------------------- Criando dash ----------------------------------------------
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])



# ------------------------------------------ Criando Bloco Membros ------------------------------------------
cabecalho_membros = [html.Thead(html.Tr([html.Th('Matricula'), html.Th('Nome')]))
]

membro1 = html.Tr([html.Td('221007626'), html.Td('Ana Luisa Santana Dantas')])
membro2 = html.Tr([html.Td('221007813'), html.Td('Andre Emanuel Bispo da Silva')])
membro3 = html.Tr([html.Td('221038776'), html.Td('Andre Luis Bispo Galvao de Souza')])
membro4 = html.Tr([html.Td('221007887'), html.Td('Bernardo Barros Blanco')])
membro5 = html.Tr([html.Td('221007949'), html.Td('Camile Barbosa Gonzaga de Oliveira')])
membro6 = html.Tr([html.Td('221008070'), html.Td('Guilherme Resende Carmona')])
membro7 = html.Tr([html.Td('221008150'), html.Td('Joao Antonio Ginuino Carvalho')])
membro8 = html.Tr([html.Td('221007653'), html.Td('Luciano Ricardo da Silva Júnior')])
membro9 = html.Tr([html.Td('211062277'), html.Td('Matheus Duarte da Silva')])
membro10 = html.Tr([html.Td('221035068'), html.Td('Paulo Renato Medrado Roque')])

corpo_membros = [html.Tbody([membro1, membro2, membro3, membro4, membro5, membro6, membro7, membro8, membro9, membro10])]
tabela_membros = dbc.Table(cabecalho_membros + corpo_membros, size = 'sm', style = {'backgroundColor': '#060606'}) # TODO: Melhorar a estilizacao da tabela com os membros

bloco_membros = dbc.Fade(
    id = 'fade',
    children = tabela_membros,
    style = {
        'height': '40vh', 
        'marginTop': '10vh',
        'marginLeft': '5rem', 
        'width': '45rem',
    },
    is_in = False,
    appear = False,
)



# --------------------------------------- Criando Bloco de Títulos ---------------------------------------
bloco_titulo = dbc.Card(
    children = [
        dbc.CardHeader(
            html.H2(
                children = 'Trafego Aéreo no Brasil',
            )
        ),
        dbc.CardBody([
            html.P(
                children = 'Dashborad sobre o Trafego Aéreo no Brasil, desenvolvido pelos estudantes da disciplina de Algoritimos e Programação de Computadores como Trabalho Final', # TODO colocar nomes dos integrantes pra aparecer ao clicar em um botão
            ),
            dbc.Button('Mostrar membros', color = 'primary', id = 'grupo', n_clicks = 0)
        ])
    ],
    style = {
        'height': '40vh', 
        'marginTop': '20vh',
        'marginLeft': '5rem', 
        'width': '45rem',
        'backgroundColor': '#060606',
    }
)



# --------------------------------------- Criando Bloco do Gráfico 1 ---------------------------------------
bloco_g1 = dbc.Card(
    children = [
        html.H6(
            children = 'Total de decolagens por mês',
            style = dicionario_estilo_titulos_graficos
        ),
        html.Label(
            children = 'Escolha o ano',
            style = dicionario_estilo_label

        ),

        dcc.Dropdown(
            options = ['2013', '2014', '2015'],
            id = 'Ano_data_pico',
            multi = True,
            placeholder = 'Escolha o Ano',
            optionHeight = 20,
            value = 'Todos os Anos',
        ),

        html.Label(
            children ='Escolha o mês',
            style = dicionario_estilo_label

        ),

        dcc.Dropdown(
            options = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
            id = 'Mes_data_pico',
            multi = True,
            placeholder = 'Escolha o Mês',
            optionHeight = 20,
            value = 'Todos os Meses',
        ),

        dcc.Loading(
            type = 'default',
            children = dcc.Graph(
                id = 'grafico_data_pico',
                figure = criar_grafico_barras_data_pico(['2013', '2014', '2015'], ["Janeiro", 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'])
            )
        )
    ],
    style = dicionario_estilo_cards
)


# --------------------------------------- Criando Bloco do Gráfico 2 ---------------------------------------


bloco_g2 = dbc.Card(
    children = [
        html.H6(
            children = 'Números de decolagem por países',
            style = dicionario_estilo_titulos_graficos
        ),

        html.Label(
            children = 'Selecione o ano que deseja analisar',
            style = dicionario_estilo_label
        ),

        dcc.Dropdown(
            id = 'filtro_anos',
            options = ['2013', '2014', '2015'], 
            value = ['2014'], 
            multi = False,
            style = {
                'fontFamily': ['Brush Script MT', 'cursive'],
                'backgroundColor': '#111111'
            }
        ),

        html.Label(
            children = 'Selecione o mês que deseja analisar',
            style = dicionario_estilo_label
        ),

        dcc.Dropdown(
            id = 'filtro_mes',
            options = ['1','2','3','4','5','6','7','8','9','10','11','12'], 
            value = ['1'], 
            multi = False,
            style = {
                'fontFamily': ['Brush Script MT', 'cursive'],
                'backgroundColor': '#111111'
            }
        ),

        html.Label(
            children = 'Selecione o país que deseja analisar',
            style = dicionario_estilo_label
        ),

        dcc.Dropdown(
            id = 'filtro_paises',
            options = ['ÁFRICA DO SUL','ARGENTINA','COLÔMBIA','ESTADOS UNIDOS DA AMÉRICA','EMIRADOS ÁRABES UNIDOS','FRANÇA','ITÁLIA','PANAMÁ','PORTUGAL','REINO UNIDO'], 
            value = ['ESTADOS UNIDOS DA AMÉRICA', 'ARGENTINA', 'FRANÇA'], 
            multi = True,
            style = {
                'fontFamily': ['Brush Script MT', 'cursive'],
                'backgroundColor': '#111111'
            }
        ),
        dcc.Loading(
            type = 'default',
            children = dcc.Graph(
                id = 'grafico_barras_paises_origem',
                # figure = cria_grafico_barras_paises_origem(['2013','2014','2015'], ['2'], ['ESTADOS UNIDOS DA AMÉRICA'])
            )
        )
    ],
    style = dicionario_estilo_cards
)



# --------------------------------------- Criando Bloco do Gráfico 3 ---------------------------------------
bloco_g3 = dbc.Card(
    children = [
        html.H6(
            children = 'Estados de destino mais escolhidos',
            style = dicionario_estilo_titulos_graficos
        ),
        html.Div([
            dbc.Label('Escolha um ano'),
            dbc.RadioItems(
                options = [
                    {'label':'2013','value':'2013'},
                    {'label':'2014','value':'2014'},
                    {'label':'2015','value':'2015'},
                ],
                value = '2013',
                id = 'escolha-ano-mapa',
                inline = True
                )
            ]
        ),
        html.Div([  
            dbc.Label('Digite uma Unidade Federativa e pressione enter'),
            dbc.Input(
                value = 'DF',
                type = 'text',
                id = 'escolha-estado-mapa',
                debounce = True,
                style = {
                    'backgroundColor': '#111111'
                }
            )
        ]
        ),
        dcc.Loading(
                type = 'default',
                children = dcc.Graph(
                    id = 'grafico-mapa',
                )
            )
        ], 
    body = True,
    style = dicionario_estilo_cards
)



# --------------------------------------- Criando Bloco do Gráfico 4 ---------------------------------------
bloco_g4 = dbc.Card(
    children = [
        html.H6(
            children = 'Empresas aéreas preferidas pelo consumidor',
            style = dicionario_estilo_titulos_graficos
        ),
        dcc.Loading(
            type = 'default',
            children = dcc.Graph(
                id = 'grafico_pizza_companhias',
            )
        ),  
        dcc.Dropdown(
            id = 'filtro_ano4s',
            options = ['2013', '2014', '2015'], 
            value ='2013',
            style = {
                'backgroundColor': '#111111'
            }
        ),
         dcc.Slider(
            id="slidermassa", min=0, max=15000000,
            marks={i: str(i/1000000)+"M" for i in range(0,15000000,1000000)},
            value=15000000
        )
    ],
    style = dicionario_estilo_cards
)

# --------------------------------------- Criando Bloco do Gráfico 5 ---------------------------------------


bloco_g5 = dbc.Card(
    children = [
        html.H6(
            id = 'titulo_grafico_pizza_tipo_carga',
            style = dicionario_estilo_titulos_graficos
        ),

        html.Label(
            children = 'Selecione os anos que deseja analizar',
            style = dicionario_estilo_label
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
        
        dcc.Loading(
            type = 'default',
            children = dcc.Graph(
                id = 'grafico_pizza_tipo_carga'
            )
        )
    ],
    style = dicionario_estilo_cards
)



# --------------------------------------------- Criando layout ---------------------------------------------
app.layout = dbc.Container([
    dbc.Row(
        children = [bloco_membros, bloco_titulo], 
        style = {
            'height': '100vh', 
            'background': 'url("/assets/fundo_dash.jpg") no-repeat', 
            'backgroundPosition': 'center', 
            'backgroundSize': 'cover'
        }
    ),

    dbc.Row([
        dbc.Col([
            dbc.Row(bloco_g1, style = dicionario_estilo_blocos)
        ], md = 5),
        dbc.Col([
            dbc.Row(bloco_g3, style = dicionario_estilo_blocos)
        ], md = 7)
    ], align = 'center'),
        
    dbc.Row([
        dbc.Col([
            dbc.Row(bloco_g5, style = dicionario_estilo_blocos)
        ], md = 5),
        dbc.Col([
            dbc.Row(bloco_g4, style = dicionario_estilo_blocos)
        ], md = 7)
    ], align = 'center'),

    dbc.Row(bloco_g2, style = dicionario_estilo_blocos, align = 'center')

], fluid = True)


# -------------------------------------- Interatividade Bloco Membros --------------------------------------
@app.callback(
    Output(component_id = 'fade', component_property = 'is_in'),
    [Input(component_id = 'grupo', component_property = 'n_clicks')],
    [State(component_id = 'fade', component_property = 'is_in')],
)
def interatividade_membros(n, is_in):
    if not n:
        return False
    return not is_in

#-----------------------------------------------I nteratividade Bloco do Gráfico 1 ---------------------------------------------------
@app.callback(
    Output(component_id='grafico_data_pico', component_property= 'figure'),
    Input(component_id='Ano_data_pico', component_property='value'),
    Input(component_id='Mes_data_pico', component_property='value'),
)
def atualizar(ano_value, mes_value):
    mes = mes_value
    ano = ano_value
    return criar_grafico_barras_data_pico((ano), (mes))


# ----------------------------------- Interatividade Bloco do Gráfico 2 ----------------------------------
@app.callback(
    Output(component_id = 'grafico_barras_paises_origem', component_property = 'figure'),
    Input(component_id = 'filtro_anos', component_property = 'value'),
    Input(component_id = 'filtro_mes', component_property = 'value'),
    Input(component_id = 'filtro_paises', component_property = 'value')
)
def interatividade_grafico_barras_paises_origem(ano, mes, paises):
    anos = [str(item) for item in [ano]]
    anos = [str(item) for item in anos]
    if ano == []:
        anos = ['2013.0', '2014.0', '2015.0']
    return cria_grafico_barras_paises_origem(anos, mes, paises)



# ----------------------------------- Interatividade Bloco do Gráfico 3 -----------------------------------
@app.callback(
        Output(component_id = 'grafico-mapa', component_property = 'figure'),
        Input(component_id = 'escolha-ano-mapa', component_property = 'value'),
        Input(component_id = 'escolha-estado-mapa', component_property = 'value')
        )
def parametrizar_mapa(ano, estado):
    figure = 0
    if not dados_validos(estado):
        figure = criar_mapa(ano)
    else:
        figure = criar_mapa(ano, estado)
    return figure

@app.callback(
        Output(component_id = 'escolha-estado-mapa', component_property = 'invalid'),
        Input(component_id = 'escolha-estado-mapa', component_property = 'value')
        )
def entrada_valida(estado):
    resultado = False
    if not dados_validos(estado):
        resultado = True
    return resultado


# ----------------------------------- Interatividade Bloco do Gráfico 4 -----------------------------------
@app.callback(
    Output(component_id = 'grafico_pizza_companhias', component_property = 'figure'),
    Input(component_id = 'filtro_ano4s', component_property = 'value'),
    Input(component_id = 'slidermassa', component_property = 'value')
)

def interacao_setores(ano,minimo):
    return  criar_setores(ano,minimo)

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
def interatividade_grafico_pizza_tipo_carga(value): # Muda os anos que serão usados na criação do gráfico
    anos = [float(item) for item in value] # Corrigindo os valores de entrada que devem ser no formato 2013.0 e não 2013
    anos = [str(item) for item in anos]
    if value == []: # No caso especifico do usuario limpar o Dropdown deve mostrar por padrao todos os anos
        anos = ['2013.0', '2014.0', '2015.0']
    return cria_grafico_pizza_tipo_carga(anos)


# ------------------------------------------ Colocando dash no ar ------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)