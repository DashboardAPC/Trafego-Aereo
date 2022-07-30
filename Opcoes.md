# Esse arquivo contem as opcoes de dataset/tema que foram discutidas no grupo.
**Sinta-se livre para modificar esse arquivo, adicionar ideias ou novas opcoes.**

## Game of Thrones
- **Todas as falas de GoT:** https://www.kaggle.com/datasets/gunnvant/game-of-thrones-srt
- **Tamanho:** 757kB
- **Ideias:** Podemos fazer um dashboad que exibe as palavras mais faladas em cada temporada, episiodio ou na serie inteira.
Mostrar o numero do episodio, a minutagem e mais qualquer dado que parecer interressante e tambem  adicionar uma opcao para o usuario entrar a palavra ou frase que ele quer saber as estatisticas.
- **OBS:** As falas estao todas em ingles, o dataset esta formatado em dicionario python (.json), provavelmente precisariamos ter filtros para palavras como 'of', 'the', 'a', etc... 
Adicionalmente se fizermos um dash com esse tema temos muitos outros datasets disponiveis como por exemplo a quantidade de aparicoes na serie, a avaliacao Imdb dos episodios e o numero de mortes por episodio.
Tambem tem esse (https://www.kaggle.com/datasets/rezaghari/game-of-thrones?select=characters_v4.csv) com MUITA informacao tipo arvore genealogica, localizacao, etc...
Enquanto escrevia isso acabei de achar o script e esse tem o nome do personagem que disse a fala junto em (https://www.kaggle.com/datasets/albenft/game-of-thrones-script-all-seasons)

## Among Us
- **Estatisticas da Gameplay de AmongUs:** https://www.kaggle.com/datasets/mrisdal/among-us-gameplay
- **Tamanho:** 290kB
- **Ideias:** Podemos elencar a taxa de sucesso dos jogadores e mostrar o que faz um jogador bom de impostor, um bom jogador de tripulante, tem informacoes sobre os votos entao podemos mostrar quais jogadores votaram certo (em prol do time que estao) e quais votaram errado, etc...
- **OBS:** Acho que esse tema eh o melhor no quesito design, ja que a gente pode 'pegar emprestado' os elementos do proprio jogo pra fazer um dashboard bunitinho e a assim facilitaria nosso trabalho. O principal problema eh que as base de dados disponiveis nao sao muito ricas. A do link acima por exemplo eh bem pequena, tem uma amostra de apenas 300 jogadores. Precisamos checar se o professor tem alguma exigencia no tamanho do dataset.
Tambem tem o https://www.kaggle.com/datasets/ruchi798/among-us-dataset mas ele eh pior no quesito tamanho amostara ja que sao so 29 jogadores mas registrando 100 partidas de cada.

## Voos no aeroportos
- **Voos nos aeroportos - Brasil** (https://gov.br/anac/pt-br/assuntos/dados-e-estatisticas/dados-estatisticos
- **Ideias:** Fazer um mapa com os destinos mais desejados, colocar estatisticas sobre as bagagem paga e nao paga.
- **OBS:** Tambem existe a posssibilidade de analizar os voos dometicos dos EUA.
Os dados do BR no site da anac estao em arquivos separados por ano, entao teriamos um trabalho de arrumar o dataset.
Temos esse dataset alternativo (https://www.kaggle.com/datasets/ramirobentes/flights-in-brazil) mas o primeiro link da anac tem mais informacoes.