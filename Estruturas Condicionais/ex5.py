""""Crie um algoritmo para resolver equações do 2º grau.
Considere:
ax2 + bx + c = 0 (a deve ser diferente de 0)
delta = b2 - 4 * a * c
Caso: delta < 0, não existe raiz real
delta = 0, existe uma raiz real: x = (-b) / (2 * a)
delta > 0, existem duas raízes reais:
x1 = (- b + raiz quadrada de delta) / (2 * a)
x2 = (- b - raiz quadrada de delta) / (2 * a)"""

import math

a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))

delta = b**2 - 4*a*c
print(f"delta: {delta}")

if(delta < 0):
    print(f"Não existe raiz real")

elif(delta == 0):
    raiz = -b/(2*a)
    print(f"apenas 1 raiz real: {raiz}")

elif(delta > 0):
    raiz1 = (-b + math.sqrt(delta))/(2*a)
    raiz2 = (-b - math.sqrt(delta))/(2*a)
    print(f"2 raizes reais: {raiz1}, {raiz2}")
    