"""Faça uma função que receba 2 listas de valores inteiros e retorne a lista
INTERSECÇÃO"""

def montaLista(lista):
    tamanhoLista = int(input("tamanho da lista: "))
    for i in range(tamanhoLista):
        elemento = input(f"insira o elemento {i}: ")
        lista.append(elemento)

def elementoNaLista(lista, elemento):
    for i in range(len(lista)):
        if elemento == lista[i]:
            return True
    return False

def interseccao(lista1, lista2, listaInterseccao):
    # So coloca os elementos que estao nos 2
    for i in range(len(lista2)):
        if elementoNaLista(lista1, lista2[i]):
            listaInterseccao.append(lista2[i])

def main():
    lista1 = []
    print("lista 1: ")
    montaLista(lista1)

    lista2 = []
    print("lista 2: ")
    montaLista(lista2)

    listaInterseccao = []
    interseccao(lista1, lista2, listaInterseccao)
    print(listaInterseccao)

if __name__ == "__main__":
    main()
