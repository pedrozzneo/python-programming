
def montarMatrizUsuario(quantidadeLinhas, quantidadeColunas):
    matriz = []
    for i in range(quantidadeLinhas):
        linha = []
        for j in range(quantidadeColunas):
            elemento = int(input(f"elemento {i}{j}: "))
            linha.append(elemento)
        matriz.append(linha)
    print()
    return matriz

def exibirMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print()
    print()

def maiorElementoMatriz(matriz):
    maior = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
    return maior
                
def menorElementoMatriz(matriz):
    menor = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < menor:
                menor = matriz[i][j]
    return menor

def ehSimetrica(matriz):
    # Percorre matriz sempre comparando com a posicao transposta
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True
            
def gerarTransposta(matriz):
    matrizTransposta = []
    for i in range(2):
        linha = []
        for j in range(3):
            linha.append(matriz[j][i])
        matrizTransposta.append(linha)
    return matrizTransposta

def contaLinhasZeradas(matriz):
    # Trava linha a linha e verifica se pelo menos 1 elemento não é zero
    linhasZeradas = 0
    for i in range(len(matriz)):
        todosZero = True
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                todosZero = False
        if todosZero:
            linhasZeradas += 1
    return linhasZeradas

def contaColunasZeradas(matriz):
    # Trava linha a coluna e verifica se pelo menos 1 elemento não é zero
    colunasZeradas = 0
    quantidadeLinhas = len(matriz)
    quantidadeColunas = len(matriz[0])
    
    for j in range(quantidadeColunas):
        todosZero = True
        for i in range(quantidadeLinhas):
            if matriz[i][j] != 0:
                todosZero = False
                break
        if todosZero:
            colunasZeradas += 1
    return colunasZeradas

def pegarColuna(matriz, j):
    coluna = []
    # Com o j travado, eu pego todas as variacoes i dele
    for i in range(len(matriz)):
        coluna.append(matriz[i][j])
    return coluna

def produtoLinhaColuna(linha, coluna):
    if len(linha) != len(coluna):
        print("Não é possível fazer a multiplicacao")
        return
    else:
        print(linha, end = " * ")
        print(coluna)
        soma = 0
        for i in range(len(linha)):
            somaParcial = 0
            somaParcial += linha[i] * coluna[i]
            print(f"{linha[i]} * {coluna[i]} = {somaParcial}")
            soma += somaParcial
        print(soma, end = "\n\n")
        return soma
    
def produtoMatricial(matrizA, matrizB):
    # A matriz multiplicacao tem as linhas de A e colunas de B
    linhasA = len(matrizA)
    colunasB = len(matrizB[0])

    # Percorre a matriz C para adquirir os valores de cada termo
    matrizC = []
    for i in range(linhasA):
        linha = []
        for j in range(colunasB):
           linhaA = matrizA[i]
           colunaB = pegarColuna(matrizB, j)
           print(f"C{i}{j}: ")
           elemento = produtoLinhaColuna(linhaA, colunaB)
           linha.append(elemento)
        matrizC.append(linha)
    return matrizC
          

