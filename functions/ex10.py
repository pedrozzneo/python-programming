"""Faça uma função que receba 2 listas de valores inteiros, o modo de
saída (U:união, I:intersecção, D:diferença) e retorne a lista resultante.
Obs: a função deverá invocar as funções definida nos exercícios de 7 a
9, para calcular U, I ou D."""

import ex7
import ex8
import ex9

def menu():
    operador = "entra no while ae"
    while operador != "u" and operador != "i" and operador != "d":
        operador = (input("qual operacao voce quer? uniao (u), interseccao (i), diferenca (d): ")).lower()

        if operador != "u" and operador != "i" and operador != "d":
            print("Entre uma operacao valida!!")
    return operador

def operarConjuntos(lista1, lista2, listaResultado, operador):
    if operador == "u":
        ex7.uniao(lista1, lista2, listaResultado)
    elif operador == "i":
        ex8.interseccao(lista1, lista2, listaResultado)
    elif operador == "d":
        ex9.diferenca(lista1, lista2, listaResultado)

def main():
    lista1 = []
    print("lista 1: ")
    ex7.montaLista(lista1)

    lista2 = []
    print("lista 2: ")
    ex7.montaLista(lista2)

    listaResultado = []

    operador = menu()
    operarConjuntos(lista1, lista2, listaResultado, operador)
    print(listaResultado)

if __name__ == "__main__":
    main()