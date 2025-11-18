"""Faça um programa que solicite do usuário um valor N, representando
a dimensão de uma matriz quadrada (matriz A). Em seguida, o
programa deverá solicitar do usuário os elementos da matriz A e,
posteriormente, deverá verificar se A é simétrica. Obs: Matriz
simétrica: matriz quadrada de ordem n tal que A = At"""

import utils

def main():
    # Coleta quantas linhas e colunas o usuário deseja
    dimensao = int(input("dimensão: "))

    # Monta matriz MxN
    print("\nEntradas: ")
    matriz = utils.montarMatrizUsuario(dimensao, dimensao)

    # Exibe matriz
    print("Matriz: ") 
    utils.exibirMatriz(matriz)

    # Determina se a matriz é ou não simétrica    
    simetrica = utils.ehSimetrica(matriz)
    
    # Determina se é ou não simétrico
    if simetrica:
        print("É simétrica!")
    else:
        print("Não é simétrica!")
main()


    