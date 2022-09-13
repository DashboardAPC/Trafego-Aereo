import barras_data_pico
from dash import Dash, html,dcc 

#Iniciar o app
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Hello Dash'),

    html.Div('Teste de construção de gráficos com o dash')

    dcc.Graph(
        id='grafico-barras',
        figure=barras_data_pico.criar_barras()
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)