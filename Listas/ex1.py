"""Gere uma lista de contendo os múltiplos de 3 entre 1 e 150."""

numero = 1
multiplo3 = []

while numero <= 150:
    if numero % 3 == 0:
        multiplo3.append(numero)
    numero += 1

for i in range(len(multiplo3)):
    print(multiplo3[i], " ", end = "")