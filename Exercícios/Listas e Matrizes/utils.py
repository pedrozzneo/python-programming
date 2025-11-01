import random

def verificadorElementoRepetido(numero, matriz, linha):
    # primeira ve na linha (ainda n pertence a matriz)
    j = 0
    while j < len(linha):
        if linha[j] == numero:
            return True
        j += 1
        
    # Agora ve na matriz mesmo
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[i]):
            if matriz[i][j] == numero:
                return True
            j += 1
        i += 1
    return False

def geradorElementoNaoRepetido(matriz, linha):
    repetido = True
    while repetido:
        numero = random.randint(0, 100)

        # Verifica se o numero gerado n é repetido
        repetido = verificadorElementoRepetido(numero, matriz, linha)

    return numero

def exibeMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print()
    print()

def montaMatriz(matriz, linhas, colunas):
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            
            # Gera um numero não repetido
            numero = geradorElementoNaoRepetido(matriz, linha)
            
            # Insere o numero na linha
            linha.append(numero)
        
        # Insere a linha na matriz
        matriz.append(linha)

def achouTermoMatriz(termo, matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == termo:
                return True
    return False

def preencherListaIguais(iguais, matriz1, matriz2):
    # Percorre cada termo da matriz 1 e compara com cada termo da matriz 2
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            termo = matriz1[i][j]
            if achouTermoMatriz(termo, matriz2):
                iguais.append(termo)

def exibeLista(lista):
    for i in range(len(lista)):
        print(lista[i], end = " ")
    print("\n")
    