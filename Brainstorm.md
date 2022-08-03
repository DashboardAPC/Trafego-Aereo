# Vamos ter ideias
**Sinta-se livre para modificar esse arquivo e adicionar ideias. Afinal esse .md se chama tempestade de ideias por algum motivo. :)**
Esse eh o ponta-pe inicial no nosso trabalho. Aqui serao adicionadas as ideias dos graficos para o nosso trabalho. Dentre as quais escolheremos 5 para fazerem parte do nosso Dashboard.
Veja o modelo dos graficos ja propostos, leia e entenda o dataset e elabore sua ideia com base nos dados presentes no dataset.
- **Tema:** Trafego aereo no Brasil
- **Dataset:** https://gov.br/anac/pt-br/assuntos/dados-e-estatisticas/dados-estatisticos
- **Obs.:** Por esse ser um simples arquivo .md aqueles que nao consequiram preparar o ambiente vscode + git + github podem utilizar o proprio navegador para edita-lo. Lembrando que o branch master esta protegido, logo o commit nele nao sera possivel. Voces devem criar um novo branch, fazer todas as modificacoes que desejarem, fazer o commit das modificacoes no branch provisorio que voce criou e depois criar um pull request que sera um "pedido de combinacao" do seu branch provisorio com o branch master.

## Proposta de Grafico 1
- **Tipo de grafico:** Grafico de barras ou caso possivel grafico de mapa
- **Variaveis analizadas pelo grafico:** Aeroporto de destino, passageiros (pagos + gratis)
- **Pra que serve esse grafico:** Mostra a qual aeroporto recebeu o maior numero de passageiros, dando indicios de que se trata de um ponto de interesse (cidade turistica, centro de negocios, etc...)
- **Opcoes de filtragem do grafico:** Quando fizermos o dashbord podemos possibilitar a filtragem temporal por ano (e talvez mes) em que occoreu o voo.
- **Comentarios adicionais:** A filtragem mensal abriria margem para o grafico demonstrar quais foram os destinos favoritos em periodos festivos como carnaval por exemplo. Outro ponto a se considerar é que os aeroportos de destino que seriam considerados aptos a entrar na conta do grafico seriam apenas os que tem o Brasil como pais de destino, ou seja, existiria a necessidade de fazermos uma filtragem do dataset afim de pegar os nomes dos aeroportos de destino (excluindo os com pais destino diferente de Brasil) e contar somando quantos passagerios chegaram nesse local.