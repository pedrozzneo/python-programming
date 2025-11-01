

def escolherOpcoes():
    # Exibe todas as opções
    print("\n\n////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
    print("Opções: ")
    print("1- Inserir paciente na fila de Emergência e Urgência")
    print("2- Inserir paciente na fila de Atendimento Ambulatorial (Pouco urgente e não urgente)")
    print("3 Atender paciente com Emergência ou Urgência")
    print("4- Atender paciente no Ambulatório")
    print("5 Imprimir fila de Emergência e Urgência")
    print("6 Imprimir fila de Atendimento Ambulatorial")
    print("7 Sair da aplicação \n")

    # Coleta a opção escolhida forçando uma entrada válida
    opcao = 0
    while opcao < 1 or opcao > 7:
        opcao = int(input("decisao: "))
        if opcao < 1 or opcao > 7:
            print("resposta inválida!")
    return opcao

def determinarPrioridadeEmergencial():
    # Coleta a opção escolhida forçando uma entrada válida
    opcao = 0
    while opcao != 1 and opcao != 2:
        prioridade = int(input("Selecione a prioridade (1: vermelho, 2: amarelo): "))
        if prioridade == 1:
            return "vermelho"
        elif prioridade == 2:
            return "amarelo"
        else:
            print("resposta inválida!")

def determinarPrioridadeAmbulatorial():
    # Exibe as opções de prioridade emergenciais
    print("Selecione a prioridade: \n")
    print("1- verde")
    print("2- azul")

    # Coleta a opção escolhida forçando uma entrada válida
    opcao = 0
    while opcao != 1 and opcao != 2:
        prioridade = int(input("prioridade:"))
        if prioridade == 1:
            return "verde"
        elif prioridade == 2:
            return "azul"
        else:
            print("resposta inválida!")

def imprimirEmergencial(filaVermelho, filaAmarelo):
    print("Fila Emergencial: ", end = "")

    # Imprime primeiro a fila vermelha
    for i in range(len(filaVermelho)):
        print(filaVermelho[i], end="")

    # Imprime depois a fila amarelo
    for j in range(len(filaAmarelo)):
        print(filaAmarelo[j], end="")
    print()

def imprimirAmbulatorial(filaVerde, filaAzul):
    print("Fila Ambulatorial: ", end = "")

    # Imprime primeiro a fila verde
    for i in range(len(filaVerde)):
        print(filaVerde[i], end="")

    # Imprime depois a fila azul
    for j in range(len(filaAzul)):
        print(filaAzul[j], end="")
    print()

def determinarCodigoPacienteEmergencial(prioridade, filaVermelho, filaAmarelo):
    # Coloca no formato correto usando as quantidades de cada tipo
    if prioridade == "vermelho":
        return "VE" + str(len(filaVermelho) + 1)
    elif prioridade == "amarelo":
        return "AM" + str(len(filaAmarelo) + 1)
    
def determinarCodigoPacienteAmbulatorial(prioridade, filaVerde, filaAzul):
    # Coloca no formato correto usando  as quantidades de cada tipo
    if prioridade == "verde":
        return "VER" + str(len(filaVerde) + 1)
    elif prioridade == "azul":
        return "AZ" + str(len(filaAzul) + 1)

def inserirListaEmergencial(filaVermelho, filaAmarelo):
    # Determina a cor (prioridade) e portanto o código
    prioridade = determinarPrioridadeEmergencial()
    codigoPaciente = determinarCodigoPacienteEmergencial(prioridade, filaVermelho, filaAmarelo)

    # Insere na fila adequada
    if prioridade == "vermelho":
        filaVermelho.append(codigoPaciente)
    elif prioridade == "amarelo":
        filaAmarelo.append(codigoPaciente)

def inserirListaAmbulatorial(filaVerde, filaAzul):
    # Determina a cor (prioridade) e portanto o código
    prioridade = determinarPrioridadeAmbulatorial()
    codigoPaciente = determinarCodigoPacienteAmbulatorial(prioridade, filaVerde, filaAzul)

    # Insere na fila adequada
    if prioridade == "verde":
        filaVerde.append(codigoPaciente)
    elif prioridade == "azul":
        filaAzul.append(codigoPaciente)

def atenderEmergencial(filaVermelho, filaAmarelo):
    # Primeiro tira do vermelho se tiver
    if len(filaVermelho) > 0:
        del filaVermelho[len(filaVermelho) - 1]
        return
    
    # Caso nao tenha tira do amarelo se tiver
    elif len(filaAmarelo) > 0:
        del filaAmarelo[len(filaAmarelo) - 1]
        return
    
    # Caso que nao tem nenhum
    else:
        print("Nao tem ninguem para atender")

def atenderAmbulatorial(filaVerde, filaAzul):
    # Primeiro tira do vermelho se tiver
    if len(filaVerde) > 0:
        del filaVerde[len(filaVerde) - 1]
        return
    
    # Caso nao tenha tira do amarelo se tiver
    elif len(filaAzul) > 0:
        del filaAzul[len(filaAzul) - 1]
        return
    
    # Caso que nao tem nenhum
    else:
        print("Nao tem ninguem para atender")

def main():
    filaVermelho = []
    filaAmarelo = []
    filaVerde = []
    filaAzul = []

    opcao = 0
    while opcao != 7:
        opcao = escolherOpcoes()
        
        if opcao == 1:
            inserirListaEmergencial(filaVermelho, filaAmarelo)
        elif opcao == 2:
            inserirListaAmbulatorial(filaVerde, filaAzul)
        elif opcao == 3:
            atenderEmergencial(filaVermelho, filaAmarelo)
        elif opcao == 4:
            atenderAmbulatorial(filaVerde, filaAzul)   
        elif opcao == 5:
            imprimirEmergencial(filaVermelho, filaAmarelo)
        elif opcao == 6:
            imprimirAmbulatorial(filaVerde, filaAzul)
main() 