"""Faça uma função recursiva para calcular
a sequência de Fibonacci."""

# Função que calcula e exibe a sequência de Fibonacci
def fibonacci(occurances, limit, prev, current, total):
    if occurances == limit:
        print(f" = {total}")
        return total
    else:
        next = current + prev
        print(f"+ {next} ", end = "")
        total += current + prev
        occurances += 1
        prev = current
        current = next
        return fibonacci(occurances, limit, prev, current, total)

# Função que retorna o n-ésimo número de Fibonacci
def FIB(n):
    if n == 0:
        return 0
    elif n== 1:
        return 1
    else:
        return FIB(n-1) + FIB(n-2)

def main():
    # Entrada do limite de ocorrências
    limit = int(input("enter the occurances of fibonacci: "))

    # Exibição da sequência de Fibonacci
    print("1 + 1 ", end = "")
    fibonacci(2, limit, 1, 1, 2)
    print(FIB(8))
main()