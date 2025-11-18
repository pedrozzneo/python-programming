"""Faça uma função que receba 2 listas de valores inteiros e retorne a lista
DIFERENÇA."""

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

def diferenca(lista1, lista2, listaDiferenca):
    # Só adiciona os elementos de 1 que nao estao em 2 (seriam eliminados)
    for i in range(len(lista1)):
        if elementoNaLista(lista2, lista1[i]) == False:
            listaDiferenca.append(lista1[i])

def main():
    lista1 = []
    print("lista 1: ")
    montaLista(lista1)

    lista2 = []
    print("lista 2: ")
    montaLista(lista2)

    listaDiferenca = []
    diferenca(lista1, lista2, listaDiferenca)
    print(listaDiferenca)

if __name__ == "__main__":
    main()

