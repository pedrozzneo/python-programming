"""Escreva um programa que leia inteiros positivos m e n e os elementos
de uma matriz A de números inteiros de dimensão m x n e ao final
mostra a quantidade de linhas e colunas que tem apenas zeros (linhas
nulas e colunas nulas)"""

import utils

def main():
    # Coleta quantas linhas e colunas o usuário deseja
    quantidadeLinhas = int(input("linhas: "))
    quantidadeColunas = int(input("Colunas: "))

    # Monta matriz MxN
    print("\nEntradas: ")
    matriz = utils.montarMatrizUsuario(quantidadeLinhas, quantidadeColunas)

    # Exibe matriz
    print("Matriz: ") 
    utils.exibirMatriz(matriz)

    # Exibe quantidade de linhas e colunas zeradas
    print(f"linhas zeradas: {utils.contaLinhasZeradas(matriz)}")
    print(f"colunas zeradas: {utils.contaColunasZeradas(matriz)}")
main()