from cProfile import label
from multiprocessing.sharedctypes import Value
from statistics import multimode
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Output, Input
from barras_data_pico import criar_grafico_barras_data_pico
import tabela_utils

app = Dash(__name__)
app.layout = html.Div([

    html.H1(children= 'Escolha o ano'),
    dcc.Dropdown(
    options= ['2013', '2014', '2015'],
    id='Ano_data_pico',
    multi= True,
    placeholder= 'Escolha o Ano',
    optionHeight= 20,
    value='Todos os Anos',
    ),

    html.H2(children= 'Escolha o mês',
    ),
    dcc.Dropdown(
    options= ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    id='Mes_data_pico',
    multi= True,
    placeholder= 'Escolha o Mês',
    optionHeight= 20,
    value= 'Todos os Meses',
    ),

    dcc.Graph(
        id='grafico_data_pico',
        figure= criar_grafico_barras_data_pico(['2013', '2014', '2015'], ["Janeiro", 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'])
    ),
])

@app.callback(
    Output(component_id='grafico_data_pico', component_property= 'figure'),
    Input(component_id='Ano_data_pico', component_property='value'),
    Input(component_id='Mes_data_pico', component_property='value'),
)
def atualizar(ano_value, mes_value):
    mes = mes_value
    ano = ano_value
    return criar_grafico_barras_data_pico((ano), (mes))

if __name__ == '__main__':
    app.run_server(debug=True)


    
        


