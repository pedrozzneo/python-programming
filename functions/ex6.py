"""Faça uma função que calcule o fatorial de um número inteiro positivo
fornecido como parâmetro. Use a função definida no exercício 1) para
verificar se o número é inteiro positivo. A função deverá retornar o
fatorial do número, ou False (caso não seja um inteiro positivo). O
resultado (ou a mensagem) deve ser impresso pelo programa principal."""

import ex1

def fatorial(numero):
    fatorial = 1
    i = 0
    while numero - i > 1:
        fatorial *= (numero-i)
        i += 1
    return fatorial

def numeroValido():
    numero = "entra no while ae"
    while ex1.inteiroPositivo(numero) == False:
        numero = input("numero que será transformado em fatorial: ")

        if ex1.inteiroPositivo(numero) == False:
            print("entre um numero inteiro positivo!!")
        else:
            return int(numero)

def main():
    numero = numeroValido()
    print(f"fatorial: {fatorial(numero)}")
main()
