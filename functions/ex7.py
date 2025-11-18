"""Faça uma função que receba 2 listas de valores inteiros e retorne a lista
UNIÃO"""

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

def uniao(lista1, lista2, listaUniao):
    # Adiciona todos de 1
    for i in range(len(lista1)):
        listaUniao.append(lista1[i])

    # já  adicionei os elementos de 1, agora só resta adicionar os de 2 SEM repetir
    for i in range(len(lista2)):
        if elementoNaLista(listaUniao, lista2[i]) == False:
            listaUniao.append(lista2[i])

def main():    
    lista1 = []
    print("lista 1: ")
    montaLista(lista1)

    lista2 = []
    print("lista 2: ")
    montaLista(lista2)

    listaUniao = []
    uniao(lista1, lista2, listaUniao)
    print(listaUniao)
    
if __name__ == "__main__":
    main()


