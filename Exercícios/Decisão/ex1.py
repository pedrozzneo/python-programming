"""A organização da OIBR, Olimpíada Internacional de Basquete de
Robô, está começando a ter problemas com dois times: os Bit
Warriors e os Byte Bulls. É que os robôs desses times acertam quase
todos os lançamentos, de qualquer posição na quadra! Pensando
bem, o jogo de basquete ficaria mesmo sem graça se jogadores
conseguissem acertar qualquer lançamento, não é mesmo? Uma
das medidas que a OIBR está implantando é uma nova pontuação
para os lançamentos, de acordo com a distância do robô para o
início da quadra. A quadra tem 2000 centímetros de comprimento,
como na figura.
Dada a distância D do robô até o início da quadra, onde está a cesta, a
regra é a seguinte:
 Se D ≤ 800, a cesta vale 1 ponto;
 Se 800 < D ≤ 1400, a cesta vale 2 pontos;
 Se 1400 < D ≤ 2000, a cesta vale 3 pontos.
Restrição: 0 ≤ D ≤ 2000
A organização da OIBR precisa de ajuda para automatizar o placar do
jogo. Dado o valor da distância D, você deve escrever um programa para
calcular o número de pontos do lançamento."""

placarWarriors = 0
placarBulls = 0
stop = False

while not stop:
    # Exibicao do placar
    print(f"\nPlacar \n Warriors: {placarWarriors} \n Bulls: {placarBulls} \n\n")

    # Coleta de dados (quem pontou)
    time = input("Qual time pontuou? \n 1- Warrios \n 2- Bulls \n 3- Acabou o jogo \n R: ")
    distancia = int(input("qual a distancia? (0 a 2000): "))

    # Condicao de existencia
    while(distancia < 0 or distancia > 2000):
        distancia = int(input("entrada invalida, qual a distancia? (0 a 2000): "))
        
    # Pontuacao pela distancia
    if(distancia <= 800):
        pontuacao = 1
    elif(distancia <= 1400):
        pontuacao = 2
    else:
        pontuacao = 3

    if(time == "1"):
        placarWarriors += pontuacao
    
    if(time == "2"):
        placarBulls += pontuacao