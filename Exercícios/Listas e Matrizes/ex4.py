"""Na teoria dos sistemas, o elemento MINMAX de uma matriz é o maior elemento
da linha em que se encontra o menor elemento da matriz. Elabore um programa
que carregue uma matriz 4 x 5 com números reais, identifique e mostre o
MINMAX e a sua posição na matriz. """

# primeiro achar o menor, ver a linha dele e então achar o maior dessa mesma linha

matriz = []
menor = 1000000000000

# Monta matriz ja procurando o menor termo
for i in range(4):
    linha = []
    for j in range(5):
        numero = int(input(f"insira o elemento {i}{j}: "))
        linha.append(numero)

        # Ve se o numero é menor, guarda seu valor (para comparar com os outros) e sua linha (para usar depois)
        if numero < menor:
            menor = numero
            linhaMenor = i
            
    matriz.append(linha)

# Acha o menor termo naquela linha
maior = matriz[linhaMenor][0]
for j in range(5):
    if matriz[linhaMenor][j] > maior:
        maior = matriz[linhaMenor][j]
        colunaMaior = j


print(f"MINMAX: {maior} na posicao {linhaMenor}{colunaMaior} ")