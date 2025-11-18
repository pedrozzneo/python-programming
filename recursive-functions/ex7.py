"""Faça uma função recursiva para calcular o quociente
da divisão inteira."""

# Função que retorna o quociente inteiro
def quociente(numero, divisor):
    if numero < divisor:
        return 0
    else:
        return 1 + quociente(numero-divisor, divisor)
    
def main():
    # Entrada de numero e divisor
    numero = int(input("numero: "))
    divisor = int(input("divisor: "))

    # exibição do quociente inteiro
    print(f"quociente da divisão inteira de {numero} por {divisor}: {quociente(numero, divisor)}") 
main()