"""Faça um programa que crie uma lista com 10 números inteirosfornecidos pelo usuário. Após criar a lista, o programa deveráimprimir:
 O maior elemento da lista
 O menor elemento da lista
 A soma de todos os elementos da lista
 Os elementos ímpares
 Os elementos maiores do que 18"""

numeros = []
soma = 0
impares = 0
maiores18 = 0
maior = 0
menor = 0    

# Entradas
i = 0
while i < 10:
    numero = int(input(f"entre o numero {i + 1}: "))
    numeros.append(numero)

    i += 1
print(f"numeros: {numeros}")

# Maior
i = 0
while i < 10:
    if(i == 0):
        maior = numeros[i]

    elif(numeros[i] > maior):
        maior = numeros[i]

    i += 1
print(f"maior: {maior}")

# Menor
i = 0
while i < 10:
    if(i == 0):
        maior = numeros[i]

    elif(numeros[i] < menor):
        menor = numeros[i]

    i += 1
print(f"menor: {menor}")

# Soma
i = 0
while i < 10:
    soma += numeros[i]

    i += 1
print(f"soma: {soma}")

# Impares
i = 0
while i < 10:
    if(numeros[i] % 2 == 1):
        impares += 1
    i += 1
print(f"impares: {impares}")

# Maiores que 18
i = 0
while i < 10:
    if(numeros[i] > 18):
        maiores18 += 1

    i += 1
print(f"maiores18: {maiores18}")








