"""Escreva um programa que remove todas as ocorrências de uma letra de
uma string. A string e a letra devem ser fornecidas pelo usuário."""

palavra = input("palavra: ")
letra = input("letra para eliminar: ")

i = 0
while i < len(palavra):
    if letra == palavra[i] and (i+1) < len(palavra):
        palavra = palavra[:i] + palavra[i+1:]
    elif letra == palavra[i] and i+1 == len(palavra):
        palavra = palavra[:i]
    i += 1

print(palavra)