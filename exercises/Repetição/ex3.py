""""Faça um programa que leia três notas de provas de uma turma de 50 alunos (3
notas para cada aluno). Para cada aluno, o programa deve calcular a média
ponderada como segue: Média = (nota1*2 + nota2*4 + nota3*3 ) / 10. Além de
mostrar a média de cada aluno, o programa deve mostrar uma mensagem
"Aprovado", caso a média seja maior ou igual a 6,0, e uma mensagem
"Reprovado", caso contrário. Ao final, o programa deve calcular e apresentar a
média geral da turma."""

for aluno in range(1, 51):
    print(f"\naluno {aluno}")
    nota1 = float(input(f"nota 1: "))
    nota2 = float(input(f"nota 2: "))
    nota3 = float(input(f"nota 3: "))

    # Perguntar pra professora pois a escala está 9/10 e nao 10/10
    media = (nota1*3 + nota2*4 + nota3*3) / 10

    print(f"media: {media}")

    if media >= 6:
        print("Aprovado")
    else:
        print("Reprovado")

        
   