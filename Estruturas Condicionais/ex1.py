""""Faça um programa que receba 5 números inteiros e informe o maior
entre eles."""

def general(quantity):
    numbers = []
    maior = -1000000000

    for i in range(0, quantity):
        number = int(input(f"Enter number {i + 1}: "))
        numbers.append(number)

        if(number > maior):
            print(f"{number} is the greatest so far")
            maior = number
        else:
            print(f"{number} is NOT greater than {maior}")
    
    print(numbers)
    print(f"The largest number is: {maior}")

#general(5)

maior = int(input("enter the number 1: "))

number2 = int(input("enter the number 2: "))
if(number2 > maior):
    maior = number2

number3 = int(input("enter the number 3: "))
if(number3 > maior):
    maior = number3

number4 = int(input("enter the number 4: "))
if(number4 > maior):
    maior = number4

number5 = int(input("enter the number 5: "))
if(number5 > maior):
    maior = number5

print(f"o maior numero e: {maior}")
