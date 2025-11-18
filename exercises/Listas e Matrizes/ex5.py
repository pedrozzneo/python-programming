"""Faça um programa que preencha uma matriz 7 x 7 de inteiros e crie duas listas
com 7 posições cada que contenham, respectivamente, o maior elemento de cada
linha e o menor elemento de cada linha. """

# Monta matriz 1 já vendo o maior e menor de cada linha
matriz1 = []
maiorM1 = []
menorM1 = []
for i in range(7):
    linha = []
    maior = -100000000000
    menor = 1000000000000

    for j in range(7):
        elemento = int(input(f"Elemento {i}{j}: "))
        linha.append(elemento)

        if(elemento > maior):
            maior = elemento
            
        if(elemento < menor):
            menor = elemento

    matriz1.append(linha)
    maiorM1.append(maior)
    menorM1.append(menor)
    
print(maiorM1)
print(menorM1)

# Monta matriz 2 já vendo o maior e menor de cada linha
matriz2 = []
maiorM2 = []
menorM2 = []
for i in range(7):
    linha = []
    maior = -100000000000
    menor = 1000000000000

    for j in range(7):
        elemento = int(input(f"Elemento {i}{j}: "))
        linha.append(elemento)

        if(elemento > maior):
            maior = elemento
            
        if(elemento < menor):
            menor = elemento
    
    matriz2.append(linha)
    maiorM2.append(maior)
    menorM2.append(menor)

print(maiorM2)
print(menorM2)