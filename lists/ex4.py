"""Crie um programa que leia inicialmente uma sequencia de N númerosinteiros. Depois, o programa deve gerar e mostrar 2 novas listas apartir da primeira: uma sem repetição de elementos e outra com oselementos que se repetem na lista original."""

# Percorre a lista termo a termo imprimindo eles
def exibe(listaOriginal):
    for i in range(len(listaOriginal)):
         print(listaOriginal[i], end = " ")
    
    # Quebra de linha para separação visual
    print()

# Coleta quantos termos o usuário gostaria de incluir e pede os valores 1 a 1 inserindo na lista
def montaListaOriginal():
    termos = int(input("termos: "))
    lista = []
    for i in range(termos):
        lista.append(int(input(f"termo {i + 1}: ")))
    return lista

# Monta as listas com e sem repeticao ao percorrer a lista original e fazer inclusões únicas em cada uma delas
def montaOutrasListas(listaOriginal):
    listaComRepeticao = []
    listaSemRepeticao = []
    for i in range(len(listaOriginal)):
        elemento = listaOriginal[i]

        # A segunda ou mais vezes de cada termo vai aqui
        if elementoEstaNaListaSemRepeticao(elemento, listaSemRepeticao):
            # Terceira ou mais vezes cai aqui em que nao preciso dizer novamente que este elemento se repete
            if elementoEstaNaListaComRepeticao(elemento, listaComRepeticao):
                continue
            # Apenas a segunda aparição do numero cai aqui, já é o minimo pra mostrar que se repete (primeira repeticao)
            else:
                listaComRepeticao.append(elemento)

        # A primeira vez de cada termo vai aqui
        else:
            listaSemRepeticao.append(elemento) 

    return listaComRepeticao, listaSemRepeticao

# Percorre a lista com repeticao termo a termo comparando com o elemento passado
def elementoEstaNaListaComRepeticao(elemento, listaComRepeticao):
    for i in range(len(listaComRepeticao)):
        if listaComRepeticao[i] == elemento:
            return True
    return False

# Percorre a lista sem repeticao termo a termo comparando com o elemento passado
def elementoEstaNaListaSemRepeticao(elemento, listaRepetida):
    for i in range(len(listaRepetida)):
        if listaRepetida[i] == elemento:
            return True
    return False

def main():
    # Constrói a lista de N termos passado pelo usuário
    listaOriginal = montaListaOriginal()
   
    # Exibe a lista original que acabou de ser montada
    print("lista original: ", end = "")
    exibe(listaOriginal)

    # Monta a lista com e sem repetição
    listaComRepeticao, listaSemRepeticao = montaOutrasListas(listaOriginal)

    # Exibe a lista com repetição
    print("lista com repetição: ", end = "")
    exibe(listaComRepeticao)

    # Exibe a lista sem repetição
    print("lista sem repetição: ", end = "")
    exibe(listaSemRepeticao)
main()