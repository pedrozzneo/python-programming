"""Faça uma função que receba quatro valores reais (faça a consistência
usando a função definida no exercício 3 ), referentes as notas que um
aluno obteve nos bimestres. A função deve retornar a média final desse
aluno."""

import ex3

soma = 0
i = 0
while i < 4:
    # Recebe nota
    nota = input(f"insira a nota {i+1}: ")

    # Verifica se essa pode ser um float
    if ex3.real(nota) == False:
        print("insira uma nota valida!")
        i -= 1
    else:
        # Converte para float
        nota = float(nota)

        # Verifica se esse float está dentro do intervalo aceito por notas
        if nota < 0 or nota > 10:
            print("insira uma nota valida!")
            i -= 1
        else:
            soma += nota

    # Proxima iteração
    i += 1

media = soma/4
print(f"media: {media}")
