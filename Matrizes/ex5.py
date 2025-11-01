"""Escreva um programa que leia inicialmente os elementos de 2
matrizes A e B, sendo A de dimensão m x n e B de dimensão p x q. O
programa deverá criar uma matriz C, representando a matriz produto
de A e B. Ao final, o programa deve mostrar as matrizes A, B e a
matriz C."""

import utils

def main():
    # Coleta quantas linhas e colunas o usuário deseja para a matriz A
    print("\nMatriz A: (note que a quantidade de colunas informadas para A será a quantidade de linhas de B para que exista a multiplicação matricial)")
    quantidadeLinhasA = int(input("linhas: "))
    quantidadeColunasA = int(input("Colunas: "))

    # Coleta quantas colunas o usuário deseja para a Matriz B
    print("\nMatriz B:")
    quantidadeLinhasB = quantidadeColunasA
    print(f"Linhas: {quantidadeLinhasB}")
    quantidadeColunasB = int(input("Colunas: "))

    # Monta matriz A
    print("\nEntradas A: ")
    matrizA = utils.montarMatrizUsuario(quantidadeLinhasA, quantidadeColunasA)

    # Monta matriz B
    print("\nEntradas B: ")
    matrizB = utils.montarMatrizUsuario(quantidadeLinhasB, quantidadeColunasB)

    # Exibe matriz A
    print("Matriz A: ") 
    utils.exibirMatriz(matrizA)

    # Exibe matriz B
    print("Matriz B: ") 
    utils.exibirMatriz(matrizB)

    # Monta matriz C
    matrizC = utils.produtoMatricial(matrizA, matrizB)
    
    # Exibe matriz C
    print("Matriz C: ") 
    utils.exibirMatriz(matrizC)
main()