""""Escreva um programa que apresente os 5 primeiros números perfeitos. Um
número perfeito é aquele que é igual a soma dos seus divisores (por exemplo, 6 =
1+2+3 e 28= 1+2+4+7+14). """


numero = 1
qntPerfeito = 0

while qntPerfeito < 10:
    divisor = 1
    soma = 0

    while divisor <= numero/2:
        if(numero % divisor == 0):
            soma += divisor
        divisor += 1

    if(soma == numero):
        print(f"o numero {numero} é perfeito")
        qntPerfeito += 1

    numero += 1