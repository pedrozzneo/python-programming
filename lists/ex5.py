"""Crie um programa que leia inicialmente duas sequências de Nelementos cada uma e ao final mostre as duas sequências originais e asequência resultante da soma de seus elementos. Exemplo:
a=[5, 9, 0] b=[12, 34, 101] soma=[17, 43, 101]"""

N = int(input("quantidade de elementos: "))

# Monta lista 1
lista1 = []
print("Monte a lista 1: ")
for i in range(N):
    numero = int(input(f"valor do termo {i + 1}: "))
    lista1.append(numero)

# Monta lista 1
lista2 = []
print("Monte a lista 2: ")
for i in range(N):
    numero = int(input(f"valor do termo {i + 1}: "))
    lista2.append(numero)

# Monta lista 3 com a soma dos termos adjacentes
lista3 = []
for i in range(N):
    numero = lista1[i] + lista2[i]
    lista3.append(numero)

# Exibe lista 1
print("Lista 1: ", end = "")
for i in range(N):
    print(lista1[i], end = "")
print()

# Exibe lista 2
print("Lista 2: ", end = "")
for i in range(N):
   print(lista2[i], end = "")
print()

# Exibe lista 3
print("Lista 3: ", end = "")
for i in range(N):
   print(lista3[i], end = "")
print()