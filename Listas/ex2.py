"""Crie um programa que leia inicialmente uma sequência de N notas dealunos fornecidas pelo usuário e ao final mostre a sequência e suamédia aritmética. Defina um critério de parada para a entrada denotas pelo usuário."""

parar = False
notas = []

# Entradas
while not parar:
    nota = int(input("insira a nota de 0 a 10 ou -1 para finalizar: "))

    if(nota == -1):
        parar = True
    elif(nota >= 0 and nota <= 10):
        notas.append(nota)
    else:
        print("faça uma entrada válida")

# Exibe     
i = 0
for i in range(len(notas)):
    print(f"nota {i}: {notas[i]}")


somaNotas = 0
for i in range(len(notas)):
    somaNotas += notas[i]
media = somaNotas/len(notas)
print(f"media: {media}")



