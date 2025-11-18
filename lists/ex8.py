"""Crie um programa que leia inicialmente uma sequência de N elementosinteiros positivos fornecidos pelo usuário e substitua seus elementos devalor ímpar por -1 e os pares por +1. 
Ao final imprima a sequênciaoriginal e a sequência alterada."""

N = int(input("quantidade de elementos: "))
original = []

for i in range(N):
    original.append(int(input(f"valor do elemento {i}: ")))

print(f"original: {original}")

alterada = []

for i in range(N):
    if original[i] % 2 == 0:
        alterada.append(1)
    else:
        alterada.append(-1)

print(f"alterada: {alterada}")