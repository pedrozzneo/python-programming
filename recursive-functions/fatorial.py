"""Faça uma função recursiva para calcular
o fatorial de um número."""

# Função que retorna o fatorial de um número
def fatorial(total, number):
    if number > 1:
        total *= number
        return fatorial(total, (number - 1))
    return total

def main():
    # Entrada do número
    total = 1
    number = int(input("enter a number to calculate its fatorial: "))

    # Exibição do fatorial
    print(f"fatorial of {fatorial(total, number)}")
main()