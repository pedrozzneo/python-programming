"""Faça uma função recursiva para calcular o
MDC entre dois números x e y. Considere:
mdc(x; y) = y, se x >= y e x mod y = 0
 mdc(x; y) = mdc(y; x), se x < y
mdc(x; y) = mdc(y; x mod y), caso contrário"""

# Função que retorna o MDC entre dois números
def mdc(x, y, divisor):
    if x % divisor == 0 and y % divisor == 0:
        return divisor
    else:
        return mdc(x, y, divisor-1)

def main():
    # Entrada dos valores x e y
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))

    # Determinação do divisor inicial
    if x < y:
        divisor = x
    else:
        divisor = y

    # Exibição do MDC
    print(f"MDC({x}, {y}) = {mdc(x, y, divisor)}")
main()