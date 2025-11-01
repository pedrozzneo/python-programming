""""Faça um algoritmo que receba três valores A, B e C e verifica se
eles podem ser os comprimentos dos lados de um triângulo. Se
forem, mostrar se é um triângulo equilátero, isósceles ou escaleno.
Considere que:
 Para ser triângulo: cada lado é menor que a soma dos outros dois
lados.
 Triângulo equilátero: tem três lados iguais
 Triângulo isósceles: tem dois lados iguais e um diferente
 Triângulo escaleno: tem três lados diferentes"""
       
def main():    
    sides = []
    equilateral = True
    greatest = -1

    for i in range(0, 3):
        side = int(input(f"enter the {i+1} side: "))
        sides.append(side)
        
        # Check if its equilateral (start with at least 2 numbers) 
        if(i > 0 and side != greatest):
            equilateral = False
        
        if(side > greatest):
            greatest = side
            greatestId = i

    if(equilateral):
        print("EQUILETERAL TRIANGLE")

    elif(sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]):
        print("ISCOSCELES TRIANGLE")

    else:
        print(f"\nsides: {sides}")
        print(f"greatest side: {greatest}")
        sides.pop(greatestId)
        print(f"sides without greatest: {sides}")

        sum = 0
        for i in range(0, len(sides)):
            sum += sides[i]

        print(f"{greatest} vs {sum}")
        if greatest >= sum:
            print("NOT A TRIANGLE")
        else:
            print("REGULAR TRIANGLE")

lado1 = int(input("insira o lado 1: "))
lado2 = int(input("insira o lado 2: "))
lado3 = int(input("insira o lado 3: "))

# Condicoes que nao sao triangulos
if(lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2):
    print("nao eh triangulo")

# Condicao para equilatero
elif(lado1 == lado2 and lado1 == lado3):
    print("eh equilatero")

# Condicao para isosceles
elif(lado1 == lado2 or lado1 == lado3 or lado3 == lado2):
    print("eh isosceles")

# Se nao entrou em nenhum, so pode ser escaleno
else:
    print("triangulo escaleno")







