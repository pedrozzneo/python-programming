""""Escreva um programa que leia um número não determinado de valores inteiros,
calcula e apresenta: a média aritmética dos valores lidos, a quantidade de valores
positivos, a quantidade de valores negativos e o percentual de valores negativos e
positivos. Obs: o programa deverá encerrar a leitura dos números, somente
quando o usuário desejar."""

encerrar = False
soma = 0
quantidade = 0
positivos = 0
negativos = 0

while encerrar == False:
    entrada = input("escreva um numero inteiro ou escreva 'e' para encerrar: ")

    if entrada == "e":
        encerrar = True
    else:
        entrada = int(entrada)
        soma += entrada
        quantidade += 1

        if(entrada >= 0):
            positivos += 1
        else:
            negativos += 1

    print(f"media = {soma/quantidade} ")
    print(f"numeros positivos = {positivos} ({(positivos/(negativos + positivos))*100}%)")
    print(f"numeros negativos = {negativos} ({(negativos/(negativos + positivos))*100}%)")

    