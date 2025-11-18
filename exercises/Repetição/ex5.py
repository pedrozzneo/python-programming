""""Escreva um programa que leia um número n (número de termos de uma
progressão aritmética), a1 (o primeiro termo da progressão) e r (a razão da
progressão) e apresenta os n termos desta progressão, bem como a soma de todos
elementos. """

n = int(input("n: "))
a1 = int(input("a1: "))
r = int(input("r: "))

soma = 0
for i in range(n):
    soma += a1 + r*i
    print(f"added {a1 + r*i} to the sum: {soma}")

print(f"resultado: {soma}")