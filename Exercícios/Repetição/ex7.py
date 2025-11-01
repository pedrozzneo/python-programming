""""Faça um programa que calcule e apresente o mdc entre dois números"""

numero1 = int(input("insira o numero 1: "))
numero2 = int(input("insira o numero 2: "))

divisor = 2
mdc = 1

while (divisor <= numero1 and divisor <= numero2):
    while (numero1 % divisor == 0 and numero2 % divisor == 0):
        mdc *= divisor

        # ja vi que é possível dividir pelo divisor, será que tem mais? vejo a sobra se tem outros divisores em comum para mais cortes
        numero1 /= divisor
        numero2 /= divisor
    
    # Testar outros divisores
    divisor += 1

print(f"mdc: {mdc}")
