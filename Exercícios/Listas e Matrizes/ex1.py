"""Em geometria analítica, dois vetores podem ser definidos como a=<a1,a2,a3> e
b=<b1,b2,b3>. Escreva um programa que leia dois vetores a e b (duas listas) de
três posições cada e efetue o produto escalar entre eles. O produto escalar é obtido
por ab = a1b1+a2b2+a3b3. De acordo com o exemplo dado abaixo, o calculo a ser
efetuado será: 1x5+4x2+7x3
1 4 7
5 2 3 """

# Monta um vetor de "quantidadeElementos" termos
def montarVetor(quantidadeElementos):
    vetor = []
    for i in range(quantidadeElementos):
        vetor.append(int(input(f"{i + 1}: ")))
    print()
    return vetor

# Realiza o produto escalar entre 2 vetores a e b
def produtoEscalar(vetor_a, vetor_b, quantidadeElementos):
    produto_escalar = 0
    for i in range(quantidadeElementos):
        mult = vetor_a[i] * vetor_b[i]
        print(f"mult {i + 1}: {vetor_a[i]} * {vetor_b[i]} = {mult}")
        produto_escalar += mult
    return produto_escalar

def main():
    quantidadeElementos = 3

    print("Vetor a: ")
    vetor_a = montarVetor(quantidadeElementos)

    print("Vetor b: ")
    vetor_b = montarVetor(quantidadeElementos)

    produto_escalar = produtoEscalar(vetor_a, vetor_b, quantidadeElementos)
    print(f"Produto Escalar: {produto_escalar}")
main()