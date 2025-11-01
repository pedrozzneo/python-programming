""""Elabore um programa que efetue a soma de todos os números ímpares que são
múltiplos de 3 e que se encontram no intervalo de 1 a 500"""

soma = 0
numero = 1

while numero <= 500:
    if(numero % 3 == 0 and numero % 2 == 1):
        soma += numero
        print(f"{numero} added to the sum")
    numero += 1

# I could simply include 3 and all the others + 6 untill the end