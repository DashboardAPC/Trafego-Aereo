import plotly.express as px
import plotly.graph_objects as go
import csv

with open('obitos-confirmados-covid-19.csv') as arquivo:
    leitorcsv = csv.reader(arquivo)
    cabecalho = []
    cabecalho = next(leitorcsv)
    print(cabecalho)