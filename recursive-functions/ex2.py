"""Faça uma função recursiva para calcular o
resto da divisão inteira."""

# Função que retorna o resto da divisão inteira
def module(number, divisor):
    if number < divisor:
        return number
    if number == divisor:
        return 0
    else:
        return module(number-divisor, divisor)

def main():
    # Entrada do número e do divisor
    number =int(input("number: "))
    divisor = int(input("divisor: "))

    # Exibição do resto da divisão
    print(module(number, divisor))
main()