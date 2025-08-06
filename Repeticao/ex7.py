""" Faça um programa em Python que leia um conjunto de valores
correspondentes às notas que os alunos obtiveram em uma prova de
Algoritmos. Quando o valor fornecido for um número negativo, significa
que não existem mais notas para serem lidas. Após isso seu programa
deverá:
 Escrever quantas notas são maiores ou iguais a 6.0
 Escrever quantas notas são maiores ou iguais a 4.0 e menores que 6.0
 Escrever quantos notas são menores que 4.0
 Escrever a média das notas fornecidas pelo usuário. """

maiorQue6 = 0
entre4e6 = 0
menorQue4 = 0

nota = int(input("Nota: "))

while(nota >= 0 and nota <= 10):
    
    if(nota < 4):
        menorQue4 += 1
    elif(nota < 6):
        entre4e6 += 1
    else:
        maiorQue6 += 1

    print(f"notas menores que 4: {menorQue4}")
    print(f"notas maiores ou iguais a 4 e menores que 6: {entre4e6}")
    print(f"notas maiores ou iguais a 6: {maiorQue6}")

    nota = int(input("\nNota?: "))