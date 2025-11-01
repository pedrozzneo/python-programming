"""Crie um programa que preencha uma matriz 3x3 de números inteiros e verifique
se essa matriz forma um quadrado mágico. Um quadrado mágico é formado
quando a soma dos elementos de cada linha é igual:
- à soma dos elementos de cada coluna da matriz;
- à soma dos elementos da diagonal principal;
- à soma dos elementos da diagonal secundária;
a
b

Por exemplo, veja um quadrado mágico de lado 3 cujas somas sempre são 15:
 8 3 4
 1 5 9
 6 7 2"""

def linhasIguais(soma, matriz):
    for i in range(3):
        somaAtual = 0
        for j in range(3):
            somaAtual += matriz[i][j]

        if somaAtual != soma:
            print("Linhas iguais: False")
            return False
    print("Linhas iguais: True")
    return True

def colunasIguais(soma, matriz):
    for j in range(3):
        somaAtual = 0
        for i in range(3):
            somaAtual += matriz[i][j]
            
        if somaAtual != soma:
            print("Colunas iguais: False")
            return False
    print("Colunas iguais: True")
    return True

def diagonalPrincipalIgual(soma, matriz):
    somaAtual = 0
    for i in range(3):
        somaAtual += matriz[i][i]

    if somaAtual != soma:
        print("Diagonal principal igual: False")
        return False
    else:
        print("Diagonal principal igual: True")
        return True

def diagonalSecundáriaIgual(soma, matriz):
    somaAtual = 0
    contador = 0
    i = 0
    j = 2

    # Começa la da ponta, aumenta a linha e diminui coluna
    while contador < 3:
        somaAtual += matriz[i + contador][j - contador]
        contador += 1
    if somaAtual != soma:
        print("Diagonal secundária igual: False")
        return False
    else:
        print("Diagonal secundária igual: True")
        return True

def valorSequencia(matriz):
    soma = 0
    for j in range(3):
        soma += matriz[1][j]
    print(f"Sequencia: {soma}")
    return soma

# Monta um vetor de "quantidadeElementos" termos
def montarMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(int(input(f"Entre o elemento {i}{j}: ")))
        matriz.append(linha)
    return matriz

def main():
    # Monta matriz 3x3
    linhas = 3
    colunas = 3
    matriz = montarMatriz(linhas, colunas)

    # Ve o valor de uma sequencia, todas as outras tem que ter esse mesmo valor
    soma = valorSequencia(matriz)

    # Verifica se todas as condiçoes são verdadeiras
    if linhasIguais(soma, matriz) and colunasIguais(soma, matriz) and diagonalPrincipalIgual(soma, matriz) and diagonalSecundáriaIgual(soma, matriz):
        print("é magico")
    else:
        print("não é mágico")
main()