""""Faça um programa que calcule e apresente o mmc entre dois números."""

numero1 = int(input("insira o numero 1: "))
numero2 = int(input("insira o numero 2: "))

mult = numero1 * numero2
print(f"multiplicacao entre os numeros da {mult}")

divisor = 2

while (divisor <= (numero1/2) and divisor <= (numero2/2)):
    while numero1 % divisor == 0 and numero2 % divisor == 0:
        print(f"ambos os numeros sao divisiveis por {divisor}")
        mult /= divisor
        print(f"é possível simplificar o mult por esse divisor: {mult}")

        # ja vi que é possível dividir pelo divisor, será que tem mais? vejo a sobra se tem outros divisores em comum para mais cortes (pensa no que sobra depois de n1 e n2 apos multiplicar e dividir, da pra simplificar por coisas em comum)
        numero1 /= divisor
        numero2 /= divisor

    # Testar outros divisores
    divisor += 1

print()