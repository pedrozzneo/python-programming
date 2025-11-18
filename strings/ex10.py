"""Escreva um programa que solicite ao usuário a entrada de um número
inteiro positivo ou negativo e mostre a quantidade de dígitos desse
número."""

numero = input("numero: ")

if numero[0] == "-":
    print(f"digitos: {len(numero)-1}")
else:
    print(f"digitos: {len(numero)}")