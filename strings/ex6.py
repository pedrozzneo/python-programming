"""Faça um programa que solicite o nome do usuário e imprima-o na
vertical e em formato de escada. """

nome = input("nome: ")

for i in range(len(nome)):
    print(nome[:i+1])