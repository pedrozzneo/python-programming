"""Faça uma função recursiva para encontrar a
soma dos elementos de uma lista L de
tamanho n.
– Se definirmos a soma dos valores de L por s(k),
com indices de 0 a k (L[0..k]), podemos escrever:
s(0) = L[0]
s(k) = s(k-1) + L[k], 1 <= k < n"""

# Função que retorna a soma dos elementos de uma lista
def sum(list, index):
    if index == 0:
        return list[0]
    else:
        return list[index] + sum(list, index-1)

def main():
    # declara a lista e coleta quantos termos ela terá
    list = []
    n = int(input("n: "))

    # Entrada dos n elementos da lista
    for i in range(n):
        list.append(int(input(f"list[{i}]: ")))

    # Exibição da soma dos elementos
    print(sum(list, 5))
main()