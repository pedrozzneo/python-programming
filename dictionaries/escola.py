def menu():
    escolha = 0
    while escolha > 8 or escolha < 1:
        print("1- incluir aluno")
        print("2- incluir prova")
        print("3- consultar provas")
        print("4- exibir média de notas de todos os alunos")
        print("5- excluir prova")
        print("6- exibir menor nota")
        print("7- exibir maior media")
        print("8- sair")

        escolha = int(input("\nEscolha: "))

        if escolha > 8 or escolha < 1:
            print("opção inválida")

    return escolha

def incluirAluno(alunos_dict):
    prontuario = input("prontuário: ")

    if prontuario in alunos_dict:
        return False
    
    nome = input("nome: ")
    email = input("email: ")
    
    notas = []
    nota = 0
    while nota != -1:
        nota = float(input("nota ou -1 para sair: "))

        if nota != -1: 
            materia = input("matéria: ")
            combo = [materia, nota]
            notas.append(combo)

    alunos_dict[prontuario] = [nome, email, notas]
    return True

def incluirProva(alunos_dict):
    prontuario = input("prontuário: ")

    if prontuario not in alunos_dict:
        return False
    
    # Adiciona as outras
    nota = 0
    while nota != -1:
        nota = float(input("nota ou -1 para sair: "))

        if nota != -1: 
            materia = input("matéria: ")
            combo = [materia, nota]
            alunos_dict[prontuario][2].append(combo)
    return True

def consultarProvas(alunos_dict):
    prontuario = input("prontuário: ")

    if prontuario not in alunos_dict:
        return False
    
    for combo in alunos_dict[prontuario][2]:
        print(f"{combo[0]}: {combo[1]}")

    print(f"media: {calcularMedia(alunos_dict[prontuario])}")
    return True

def calcularMedia(dados):
    somaNotas = 0
    
    for notas in dados[2]:
        somaNotas += notas[1]
    
    return somaNotas/len(dados[2])

def mediaALunos(alunos_dict):
    for dados in alunos_dict.values():
        media = calcularMedia(dados)

    print(media)

def excluirProva(alunos_dict):
    prontuario = input("prontuario: ")
    if prontuario not in alunos_dict:
        return False
        
    materia = input("materia: ")
    i = 0
    while i < len(alunos_dict[prontuario][2]):
        if alunos_dict[prontuario][2][i][0] == materia:
            del alunos_dict[prontuario][2][i]
            return True
    print("prontuário nao encontrado")

def exibirMenorNota(alunos_dict):
    menorNota = 11
    nomes = []

    for dados in alunos_dict.values():
        for combo in dados[2]:
            if combo[1] < menorNota:
                menorNota = combo[1]
                nome = dados[0]
                nomes = [nome]

            elif combo[1] == menorNota:
                nome = dados[0]
                nomes.append(nome)

    print(nomes, menorNota)

def exibirMaiorMedia(alunos_dict):
    maiorMedia = -1
    nomes = []

    for dados in alunos_dict.values():
        media = calcularMedia(dados)

        if media > maiorMedia:
            maiorMedia = media
            nome = dados[0]
            nomes = [nome]

        elif media == maiorMedia:
            nome = dados[0]
            nomes.append(nome)

    print(nomes, maiorMedia)

def main():
    alunos_dict = {"3053946": ["pedro", "henrique@", [["apr1", 9.5], ["fisica", 4]]], "1": ["lucas", "lucas@", [["apr1", 7]]]}
    escolha = 0
    while escolha != 8:
        escolha = menu()

        if escolha == 1:
            sucesso = incluirAluno(alunos_dict)
            if not sucesso:
                print("prontuário já em uso!")

        elif escolha == 2:
            sucesso = incluirProva(alunos_dict)
            if not sucesso:
                print("prontuário nao encontrado!")

        elif escolha == 3:
            sucesso = consultarProvas(alunos_dict)
            if not sucesso:
                print("prontuário nao encontrado!")

        elif escolha == 4:
            mediaALunos(alunos_dict)

        elif escolha == 5:
            sucesso = excluirProva(alunos_dict)
            if not sucesso:
                print("prontuário nao encontrado!")

        elif escolha == 6:
            exibirMenorNota(alunos_dict)

        elif escolha == 7:
            exibirMaiorMedia(alunos_dict)
main()