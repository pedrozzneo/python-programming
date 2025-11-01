"""O professor Rui está desenvolvendo um sistema automático para
identificar se uma cobra é uma coral verdadeira ou uma falsa coral. A
cobra coral verdadeira é venenosa e os anéis coloridos no seu corpo
seguem o padrão ...BVBPBVBPBVBP..., onde B,V e P representam as
cores branco, vermelho e preto, respectivamente. Já a falsa coral não é
venenosa e os anéis seguem o padrão ...BVPBVPBVPBVP....
O problema é que os sensores do sistema do professor Rui produzem
apenas uma sequência de quatro números representando um pedaço do
padrão de cores. Só que ele não sabe qual número representa qual cor.
Mas, por exemplo, se a sequência for 5 3 9 3, podemos dizer com certeza
que é uma coral verdadeira, mesmo sem saber qual número representa
qual cor! Você deve ajudar o professor Rui e escrever um programa que
diga se a coral é verdadeira ou falsa.
Entrada
A entrada consiste de quatro números inteiros.
Saída
Seu programa deve imprimir na saída uma linha com a letra "V" se a
coral for verdadeira ou com a letra "F", caso seja falsa.
Restrições
Os quatro números têm valores entre 1 e 9, inclusive, e a sequência
sempre representa uma coral verdadeira, ou uma coral falsa."""

# Na verdadeira o padrao se repete a cada 2 e a cada 4(descarta), na falsa a cada 3

numeros = []
for i in range(4):
    numeros.append(int(input()))

print(numeros)

i = 0
repetido = False

# Vai comparando até encontrar o repetido
while i < 4 and repetido == False:
    
    # Trava um número
    comparacao1 = numeros[i]

    # Index dos sucessores 
    j = i + 1
   
    # Tenta ver se acha algum sucessor igual
    while j < 4 and repetido == False:
        comparacao2 = numeros[j]

        if comparacao1 == comparacao2:
            repetido = True
            distancia = j - i # Variável que guarda quanto andou para repetir

        j += 1

    # Compara com os proximos
    i += 1

if distancia == 2:
    print("V")
if distancia == 3:
    print("F")