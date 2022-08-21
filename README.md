# Grupo A - Tráfego aéreo no Brasil

Esse é o nosso projeto final da disciplina de APC, onde criaremos um dashboard:  
Um painel com vários gráficos e medidas com o intuito de demonstrar um conjunto de dados sobre um certo tema.


## Integrantes
| Matrícula | Nome | Nick no GitHub |
|-----------|------|------------------|
| 221007813 | André Emanuel | Hunter104 |
| 221038776 | André Luís | Andre-galvao |
| ????????? | Ana Luísa | animaniacs003 |
| 221007887 | Bernardo Barros | BBBX9000 |
| 221007949 | Camile Oliveira | Camile1234 |
| 211062277 | Duarte | smmstakes |
| 221008070 | Guilherme | Guiizon |
| 221008150 | João | joaoseisei |
| 221007653 | Luciano Ricardo da Silva Júnior | l-ricardo |
| 221035068 | Paulo Renato Medrado Roque | paulomedrado |


## Objetivo
Analisar e compreender o comportamento de voôs no Brasil durante os anos de 2013, 2014 e 2015, além de oferecer uma representação gráfica sobre os dados explorados.


## Dataset e arquivos importantes
- [Vôos de 2013 até 2015](Dashboard-Oficial/data/ANAC20XX-13-14-15.csv), dados coletados do site da ANAC e processados conforme nossas necessidades.
- [Polígonos dos estados do brasil em forma de GeoJson](Dashboard-Oficial/data/brasil_estados.json), utilizado para a formação gráfica do mapa.
- [Utilidades de tabela](Dashboard-Oficial/src/tabela_utils.py), arquivo com funções que escrevemos que são necessários em múltiplos gráficos, evitando a repetição de código.


# Gráficos
## Mapa dos estados (Gráfico de Mapa)
[Esse gráfico](Dashboard-Oficial/src/mapa.py) é um mapa mostrando quais foram os estados de destino mais famosos durante o período escolhido, sendo possível notar diferenças socioeconômicas entre outros detalhes por estado.

## Preferência de linhas aéreas (Gráfico de Pizza)
[Esse gráfico](Dashboard-Oficial/src/setores.py) evidencia as preferências de linhas aéreas em todos os vôos relacionados ao brasil, mostrado claramente a tendência de uso das linhas nacionais.

## Tipos de carga (Gráfico de Pizza)
[Esse gráfico](Dashboard-Oficial/src/pizza_malas.py) desmostra a relação de proporcinalidade entre o peso de carga/bagagem/correio transportados pelos aviões em cada ano.

## Países de origem (Gráfico de Barras)
[Esse gráfico](Dashboard-Oficial/src/paises.py) nos comunica sobre quais países de um grupo seleto tem mais vôos com destino ao Brasil.

## Quantidade de vôos (Gráfico de Barras)
[Esse gráfico](Dashboard-Oficial/src/grafico_barras.py) demonstra claramente certas tendências quanto a quantidade de voôs no brasil, principalmente os picos em 2014, devido à copa do mundo.