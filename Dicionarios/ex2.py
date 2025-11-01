def options():
    print("\n\nOpções: ")
    print("1- incluir contato")
    print("2- incluir telefone: ")
    print("3- excluir telefone: ")
    print("4- excluir nome: ")
    print("5- consultar telefone: ")
    print("6- imprimir contatos: ")
    print("7- sair ")
    choice = int(input("Escolha: "))
    print("\n")
    return choice

def incluirContato(dictTelefones, contato):
    if contato not in dictTelefones:
        listaTelefones = []
        
        telefone = "a"
        while telefone != "s":
            telefone = input("insira o telefone ou 's' para sair: ")
            if telefone != "s":
                listaTelefones.append(telefone)
            
        if len(listaTelefones) > 0: 
            dictTelefones[contato] = listaTelefones
            return 1
        else:
            print("nenhum número foi fornecido")
            return 0
    print("contato já está na lista de telefones")
    return 0

def incluirTelefone(dictTelefones):
    contato = input("qual contato você deseja adicionar telefones? ")
    
    if contato not in dictTelefones:
        print("contato não existe no dicionário! ")
        return 0
    
    # Cria uma lista com todos os telefones que tinha, adiciona na lista o novo telefone e reatribui no dicionário
    listaTelefones = dictTelefones[contato]
    listaTelefones.append(input(f"telefone a ser inserido: "))
    dictTelefones[contato] = listaTelefones
    return 1

def excluirNome(dictTelefones, contato):
    if contato in dictTelefones:
        del dictTelefones[contato]
        return 1
    return 0

def excluirTelefone(dictTelefones, contato, numeroParaRemover):
    if contato not in dictTelefones:
        return 0

    listaTelefones = dictTelefones[contato]
    
    if len(listaTelefones) < 2:
        return excluirNome(dictTelefones, contato)
        
    i = 0
    while i < len(listaTelefones):
        if listaTelefones[i] == numeroParaRemover:
            del listaTelefones[i]
            dictTelefones[contato] = listaTelefones
            # Depois adaptar para dictTelefones[contato][i]
            return 1
        i += 1
    return 0

def consultarTelefone(dictTelefones, contato):
    if contato in dictTelefones:
        print(f"telefones associados ao {contato}: {dictTelefones[contato]} ")
        return
    print("contato não foi encontado")

def imprimirContatos(dictTelefones):
    for contato in dictTelefones.items():
        print(contato)

def handleChoice(choice, dictTelefones):
    if choice == 1:
        contato = input("nome do novo contato: ")
        return incluirContato(dictTelefones, contato)
    elif choice == 2:
        return incluirTelefone(dictTelefones)
    elif choice == 3:
        contato = input("nome do contato que será retirado o número: ")
        numero = input("numero para remover: ")
        return excluirTelefone(dictTelefones, contato, numero)
    elif choice == 4:
        contato = input("nome do contato que será removido: ")
        return excluirNome(dictTelefones, contato)
    elif choice == 5:
        contato = input("nome do contato para visualizar os telefones associados: ")
        consultarTelefone(dictTelefones, contato)
    elif choice == 6:
        imprimirContatos(dictTelefones)
    elif choice == 7:
        return 1
    
def main():
    dictTelefones = {"pedro" : ["1234"]}
    print(dictTelefones)
    choice = 0

    while choice != 7:
        choice = options()
        sucesso = handleChoice(choice, dictTelefones)

        if sucesso:
            print("operacao bem sucedida!")
        elif sucesso == 0:
            print("operacao falhou")
main()