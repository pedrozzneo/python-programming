"""A turma do colégio vai fazer uma excursão na serra e todos os alunos e
monitores vão tomar um teleférico para subir até o pico de uma
montanha. A cabine do teleférico pode levar C pessoas no máximo,
contando alunos e monitores, durante uma viagem até o pico. Por
questão de segurança, tem que ter pelo menos um monitor dentro da
cabine junto com os alunos. Por exemplo, se cabem C=10 pessoas na
cabine e a turma tem A=20 alunos, o colégio poderia fazer três viagens:
a primeira com 8 alunos e um monitor; a segunda com 6 alunos e um
monitor; e a terceira com 6 alunos e um monitor. Você consegue ver que
não seria possível fazer apenas duas viagens?
Dados como entrada a capacidade C da cabine e o número total A de
alunos, você deve escrever um programa para calcular o número
mínimo de viagens do teleférico.
Entrada
A primeira linha da entrada contém um inteiro C, representando a
capacidade da cabine. A segunda linha da entrada contém um inteiro A,
representando o número total de alunos na turma.
Saída
Seu programa deve imprimir uma linha contendo um número inteiro
representando o número mínimo de viagens do teleférico para levar
todos os alunos até o pico da montanha.
Restrições
2 ≤ C ≤ 100 e 1 ≤ A ≤ 1000"""

# Entrada C que satisfaz 2 ≤ C ≤ 100
c = 0
while c < 2 or c > 100:
    c = int(input("C: "))
    if c < 2 or c > 100:
        print("C deve estar no intervalo 2 ≤ C ≤ 100")

# Entrada A que satisfaz 1 ≤ A ≤ 1000
a = 0
while a < 1 or a > 1000:
    a = int(input("A: "))
    if a < 1 or a > 1000:
        print("A deve estar no intervalo 1 ≤ A ≤ 1000")        

# O máximo de alunos por trajeto é c-1
if a % (c-1) != 0:
    # indica que a divisao tem resto, ou seja, faltam pessoas, precisa de mais um trajeto
    trajetos = a//(c-1) + 1 
else:
    trajetos = a//(c-1)

print(trajetos)