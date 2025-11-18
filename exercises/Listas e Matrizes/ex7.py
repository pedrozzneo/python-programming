"""Escrever um programa que preencha 2 matrizes (a e b) de 3 linhas x 4 colunas com
números aleatórios e não repetidos (entre 0 e 100). Em seguida, verifique a
existência de números iguais nas duas matrizes, imprimindo-os. No exemplo a
seguir apenas o número 4 aparece em ambas matrizes.
Matriz 1
2 4 17 8
5 10 3 19
12 13 6 0
Matriz 2
12 14 27 18
75 4 53 11
52 93 61 30 """

import utils

def main():
    # Declara quantidade de linhas, colunas e as matrizes
    linhas = 3
    colunas = 4
    matriz1 = []
    matriz2 = []

    # Monta as matrizes
    utils.montaMatriz(matriz1, linhas, colunas)
    utils.montaMatriz(matriz2, linhas, colunas)

    # Exibe a Matriz1
    print("\nMatriz A: ")
    utils.exibeMatriz(matriz1)

    # Exibe a Matriz2
    print("Matriz B: ")
    utils.exibeMatriz(matriz2)

    # Verifica os termos iguais e guarda em uma lista
    iguais = []
    utils.preencherListaIguais(iguais, matriz1, matriz2)

    # Exibe os termos iguais
    print(f"Termos iguais: ", end = "")
    utils.exibeLista(iguais)
main()

