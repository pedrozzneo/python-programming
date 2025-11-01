"""Faça um programa que recebe uma frase e retorna o número de palavras
que a frase contém."""

frase = input("frase: ")

palavras = 1
for i in range(len(frase)):
    if frase[i] == " ":
        palavras += 1
    
print(f"a frase {frase} possuí {palavras} palavras")