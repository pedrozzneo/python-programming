def main():
    condicaoSatisfeita = False
    while(condicaoSatisfeita == False):
        N, M = [int(i) for i in input("Entre o numero de casas e entregas: ").split()]
        condicaoSatisfeita = verificadorNM(N, M)

    condicaoSatisfeita = False
    while(condicaoSatisfeita == False):
        numeroCasas = input("numero das casas em ordem crescente: ").split()
        condicaoSatisfeita = verificadorNumeroCasas(numeroCasas)

    ordemEntregas = input("ordem das entregas: ").split()
    distancia = 0

    # print(f"{M} {N}")
    # print(f"{numeroCasas}")
    # print(f"{ordemEntregas}")

    casaAtual = numeroCasas[0]
    distanciaTot = 0
    for casaDestino in ordemEntregas:
        posicaoCasaAtual = numeroCasas.index(casaAtual)
        posicaoCasaDestino = numeroCasas.index(casaDestino)

        distancia = posicaoCasaDestino - posicaoCasaAtual
        if(distancia < 0):
            distancia *= -1
        distanciaTot += distancia
        
        print(f"{distancia} incrementada, resultado parcial: {distanciaTot}")

        # Prepara para a proxima iteracao
        casaAtual = casaDestino

    print(f"distancia total: {distanciaTot}")

def verificadorNM(N, M):
    if(N < 1 or N > 45000 or M < 1 or M > 45000):
        print("Intervalo nao aceito, N e M devem estar entre 1 e 45000")
        return False
    return True  

def verificadorNumeroCasas(numeroCasas):
    numeroAnterior = -1
    for numero in numeroCasas:
        numero = int(numero)
        if(numero < 1 or numero > 1000000000):
            print("intervalo nao aceito, o numero deve estar entre 1 e 1000000000")
            return False
        if(numeroAnterior > numero):
            print("o numero das casas nao foram inseridas em ordem crescente! ")
            return False
        numeroAnterior = numero
    return True

main()
