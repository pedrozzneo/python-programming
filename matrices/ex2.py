"""Faça um programa que solicite do usuário os elementos de uma matriz 3
x 2 (matriz A). Em seguida, o programa deverá criar a matriz transposta
de A (A
t
). Ao final, deve ser mostrada a matriz original e sua respectiva
transposta. Lembre-se que a matriz transposta A
t
será obtida a partir da
matriz A trocando-se ordenadamente as linhas por colunas (ou as
colunas por linhas), como no exemplo a seguir:"""

import utils

def main():
    # Monta matriz 3x2
    print("\nEntradas: ")
    matriz = utils.montarMatrizUsuario(3, 2)

    # gera matriz transposta
    matrizTransposta = utils.gerarTransposta(matriz)

    # Exibe matriz
    print("Matriz: ")
    utils.exibirMatriz(matriz)

    # Exibe matriz transposta
    print("Matriz transposta: ")
    utils.exibirMatriz(matrizTransposta)
main()
