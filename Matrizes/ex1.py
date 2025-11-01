"""Crie um programa que solicita do usuário um valor N representando a
quantidade linhas e um valor M representando a quantidade de colunas
de uma matriz. Depois, o programa deverá solicitar do usuário N x M
elementos para serem incluídos na matriz. Por fim, o programa deverá
percorrer a matriz para encontrar e imprimir o seu maior elemento e o
seu menor elemento."""

import utils

def main():
    # Coleta quantas linhas e colunas o usuário deseja
    quantidadeLinhas = int(input("linhas: "))
    quantidadeColunas = int(input("Colunas: "))

    # Monta matriz MxN
    matriz = utils.montarMatrizUsuario(quantidadeLinhas, quantidadeColunas)

    # Exibe matriz
    utils.exibirMatriz(matriz)
        
    # Exibe maior e menor elemento da matriz
    print(f"maior elemento da matriz: {utils.maiorElementoMatriz(matriz)}")
    print(f"menor elemento da matriz: {utils.menorElementoMatriz(matriz)}")
main()