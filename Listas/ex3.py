"""Crie um programa que leia inicialmente uma sequência de N númerosinteiros e ao seu final mostre a sequência original, a soma de seuselementos que forem pares e a multiplicação dos elementos queforem ímpares."""

parar = False
numeros = []

# Entradas
while not parar:
    numero = input("insira um numero ou 'f' para finalizar: ")

    if(numero == 'f'):
        parar = True
    else:
        numero = int(numero)
        numeros.append(numero)

# Exibe     
i = 0
for i in range(len(numeros)):
    print(numeros[i], end= " ")
print()

# Soma dos pares
somaPares = 0
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        somaPares += numeros[i]
print(f"soma dos pares: {somaPares}")

# Multiplicação dos ímpares
multImpares = 1
for i in range(len(numeros)):
    if numeros[i] % 2 == 1:
        multImpares *= numeros[i]
print(f"mult impares: {multImpares}")