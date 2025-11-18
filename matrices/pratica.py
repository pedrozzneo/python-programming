"""Escreva um programa que crie uma lista para representar a turma de
alunos de APR1, a partir de dados fornecidos pelo usuário. Para cada
aluno deverão ser gravados os seguintes dados: nome, prontuário e
uma lista de até 4 notas.
turma=[ [nome_aluno1, pront_aluno1, [N1, N2, N3,
N4]], [nome_aluno2, pront_aluno2, [N1, N2, N3]],
...]
A quantidade de notas pode NÃO ser a mesma para todos os alunos, de
modo que você deve estabelecer um critério de parada para a entrada de
notas de cada aluno (por ex., nota negativa). Estabeleça também um
critério de parada para a inclusão de um novo aluno.
Ao final, o programa deverá calcular a média aritmética das notas de cada
aluno e apresentar o nome, o prontuário e a média de todos os alunos da
turma. Deverá apresentar também a maior e a menor média da turma,
bem como informar o nome dos alunos que tiveram a maior e menor
média."""

def montarTurma(turma):
    intencao = 1

    # Preenche dados de cada aluno enquanto o usuário possui intenção de adicionar mais
    while intencao == 1:
        nome = input("\nnome: ")
        prontuario = input("prontuario: ")
        notas = []
        nota = 5 # apenas para entrar no while

        # Se entrar nota invalida ele para de preencher até um limite de 4
        while nota >= 0 and nota <= 10 and len(notas) < 4:
            nota = float(input(f"insira a nota {len(notas) + 1} ou uma nota invalida para encerrar: "))
            if(nota >= 0 and nota <= 10):
                notas.append(nota)

        turma.append([nome, prontuario, notas])
        print(turma)
    
        # verifica se o usuário quer continuar inserindo dados
        intencao = int(input("\nDigite 1 se deseja deseja inserir mais dados ou qualquer outra coisa se deseja finalizar: "))

def calcularMedia(notas):
    somadorNotas = 0
    for i in range(len(notas)):
        somadorNotas += notas[i]
    return somadorNotas/len(notas)

def exibirNotas(notas):
    print("notas: ", end = "")   
    for i in range(len(notas)):
        print(notas[i], end = " ")   

def exibirTodasInfo(i, nome, prontuario, media, notas):
    print(f"\naluno {i+1}: \n")
    print(f"nome: {nome}")
    print(f"prontuario: {prontuario}")
    print(f"media: {media}")
    exibirNotas(notas)
    print()

def main():
    # Monta a lista turma
    turma = []
    montarTurma(turma)

    # Atribui as variáveis algum valor para elas começarem a comparar
    maiorMedia = calcularMedia(turma[0][2])
    menorMedia = maiorMedia
    alunoMaiorMedia = [turma[0][0]]
    alunoMenorMedia = [turma[0][0]]

    # Faz a determinação das variáveis pedidas para cada aluno
    for i in range(len(turma)):
        nome = turma[i][0]
        prontuario = turma[i][1]
        notas = turma[i][2]
        
        # Calcula a média desse aluno
        media = calcularMedia(notas)

        # Apenas inclui junto com a maior media pois foram iguais
        if media == maiorMedia and i != 0:
            alunoMaiorMedia.append(nome)

        # Verifica se ela é a maior até o momento e substitui
        elif media > maiorMedia:
            maiorMedia = media
            alunoMaiorMedia = [nome]

        # Apenas inclui junto com a menor media pois foram iguais
        if media == menorMedia and i != 0:
            alunoMenorMedia.append(nome)

        # Verifica se ela é a menor até o momento e substitui
        elif media < menorMedia:
            menorMedia = media
            alunoMenorMedia = [nome]

        # Exibe todas as info
        exibirTodasInfo(i, nome, prontuario, media, notas)
       
    # Exibe maior e menor média da turma assim como o nome do aluno correspondente a elas
    print(f"Maior média de valor {maiorMedia} dos alunos: {alunoMaiorMedia}")
    print(f"Menor média de valor {menorMedia} dos alunos: {alunoMenorMedia}")