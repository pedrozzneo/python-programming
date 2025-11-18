"""Faça uma função recursiva para encontrar a
potência positiva (n>=0) de um número X. """

# Função que retorna o número elevado por uma potência
def pow(number, power):
    if power == 1:
        return number
    elif power == 0:
        return 0
    else:
        return number * pow(number, power-1)

def main():
    # Entrada do número e da potência 
    number =int(input("number: "))
    power = int(input("power: "))

    # Exibição do número elevado a potência
    print(pow(number, power))
main()