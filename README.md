# Grupo A - Tráfego aéreo no brasil

Esse é o nosso projeto final da disciplina de APC, onde criaremos um dashboard:  
Um painel com vários gráficos e medidas com o intuito de demonstrar um conjunto de dados sobre um certo tema

## Dados

- Tema: Trafego aéreo no Brasil
- Objetivo: Analisar e compreender o comportamento de voôs no Brasil durante os anos de 2013, 2014 e 2015, além de oferecer uma representação gráfica sobre os dados explorados.

## Integrantes

nome (nickname do github) - matrícula

- André Emanuel (Hunter104) - 221007813
- Camile Oliveira (Camile1234)-221007949
- André Luís (Andre-galvao) 221038776
- Guilherme (Guiizon) 221008070
- Bernardo Barros (BBBX9000) 221007887
- Ana Luísa (animaniacs003)
- João (joaoseisei)-221008150
- Paulo Renato Medrado Roque (paulomedrado) - 221035068
- Duarte (smmstakes)
- Ricardo (l-ricardo)-221007653  

## Arquivos importantes

- [Vôos de 2013 até 2015](Dashboard-Oficial/data/ANAC20XX-13-14-15.csv), dados coletados do site da ANAC e processados conforme nossas necessidades
- [Polígonos dos estados do brasil em forma de GeoJson](Dashboard-Oficial/data/brasil_estados.json), utilizado para a formação gráfica do mapa
- [Utilidades de tabela](Dashboard-Oficial/src/tabela_utils.py), arquivo com funções que escrevemos que são comums para vários integrantes, evitando a repetição de código

# Gráficos

## Mapa dos estados

[Esse gráfico](Dashboard-Oficial/src/mapa.py) é um mapa mostrando quais foram os estados de destino mais famosos durante o período escolhido, sendo possível notar diferenças socioeconômicas entre outros detalhes por estado.

## Quantidade de vôos

[Esse mapa](Dashboard-Oficial/src/grafico_barras.py) demonstra claramente certas tendências quanto a quantidade de voôs no brasil, principalmente os picos em 2014, devido à copa do mundo.

## Preferência de linhas aéreas

[Esse mapa](Dashboard-Oficial/src/setores.py) evidencia as preferências de linhas aéreas em todos os vôos relacionados ao brasil, mostrado claramente a tendência de uso das linhas nacionais.

## Países

[Esse mapa](Dashboard-Oficial/src/paises.py) nos comunica sobre quais países de um grupo seleto tem mais vôos com destino ao Brasil.
