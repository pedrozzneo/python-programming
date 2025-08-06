""" Faça um programa que receba um número N fornecido pelo usuário e
mostre os N termos da série a seguir. Depois, imprima a soma total da
série.
s = 1 + 2
3 + 3
5 + 4
7 + 5
9 … + """

numero = int(input("numero: "))
numerador = 1
denominador = 1
soma = 0

while(numerador <= numero):
    soma += numerador/denominador
    print(f"somando {numerador}/{denominador}: {soma}")

    numerador += 1
    denominador += 2
