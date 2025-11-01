"""Escreva um programa que remove a primeira ocorrência de uma letra de
uma string. A string e a letra devem ser fornecidas pelo usuário."""

palavra = input("palavra: ")
letra = input("letra para eliminar: ")

i = 0
tirei = False
while i < len(palavra) and not tirei:
    if letra == palavra[i] and (i+1) < len(palavra):
        palavra = palavra[:i] + palavra[i+1:]
        tirei = True
    elif letra == palavra[i] and i+1 == len(palavra):
        palavra = palavra[:i]
        tirei = True
    i += 1

print(palavra)