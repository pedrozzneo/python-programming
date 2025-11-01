"""Faça um programa que permita ao usuário digitar o seu nome e em
seguida o mostre de trás para frente utilizando somente letras
maiúsculas."""

nome = input("nome: ")

for i in range(len(nome)):
    print(nome[-(i+1)].upper(), end = "")