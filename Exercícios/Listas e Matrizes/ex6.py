"""Crie um programa que preencha uma matriz 10 x 20 de números inteiros e some
cada uma das linhas, armazenando o resultado das somas em uma lista. Em
seguida, o programa deverá multiplicar cada elemento da matriz pelo elemento da
linha correspondente na lista e mostrar a matriz resultante. """

import utils

def main():
    # Define a quantidade de linhas, colunas e matrizes que serão utilizadas
    linhas = 3
    colunas = 3
    matriz = []
    somaLinha = []

    # Monta matriz realizando a soma de cada linha e guardando na lista
    for i in range(linhas):
        # Define a linha e somador atual
        linha = []
        soma = 0

        # Preenche a linha e intera o elemento no somador
        for j in range(colunas):
            elemento = int(input(f"Elemento {i}{j}: "))
            linha.append(elemento)
            soma += elemento
            
        # Coloca a linha na matriz e a respectiva soma na lista
        matriz.append(linha)
        somaLinha.append(soma)

    # Exibe a soma da linha
    print(f"\nsoma de cada linha: ", end = "")
    utils.exibeLista(somaLinha)

    # Multiplica cada elemento pela soma dos elementos de sua linha
    for i in range(linhas):
        for j in range(colunas):
            matriz[i][j] = matriz[i][j] * somaLinha[i]
    
    # Exibe a matriz resultante das multiplicações
    utils.exibeMatriz(matriz)
main()