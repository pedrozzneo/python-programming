""" Faça um programa que leia um número inteiro >= 0 e calcule o seu
fatorial. """

numero = int(input("numero: "))
fatorial = 1

while(numero > 1):
    fatorial *= numero
    numero -= 1    

print(f"{numero} fatorial: {fatorial}")
