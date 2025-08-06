"""Faça um programa em Python que receba dois valores inteiros,
representando a base e o expoente. O programa deverá calcular e
apresentar o resultado da base elevada ao expoente. Por exemplo, para
base = 5 e expoente = 3, ou seja, 53
, o programa deverá imprimir 125.
 Obs: não utilize o operador de exponenciação (**). Utilize somente estrutura de
repetição."""

base = int(input("valor da base: "))
expoente = int(input("valor da expoente: "))
resultado = 1

contador = 0
while(contador < expoente):
    resultado *= base
    contador += 1
    
print(f"resultado: {resultado}")