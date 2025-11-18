""""Faça um programa que calcule e escreva a soma dos 20 primeiros termos da série:
100/0! + 99/1! + 98/2!..."""

def resultadoFatorial(denominador):
    fatorial = 1

    while denominador > 1:
        fatorial *= denominador
        denominador -= 1

    return fatorial

def main(): 
    numerador = 100
    denominador = 0
    contador = 0
    soma = 0

    while contador < 20:
        fatorial = resultadoFatorial(denominador)
        soma += numerador/fatorial
        print(f"soma incluiu {numerador}/{fatorial}!: {soma}")

        denominador += 1
        numerador -= 1
        contador += 1

main()
