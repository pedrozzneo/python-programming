""""Escreva um programa que leia três números inteiros e os imprima em
ordem crescente."""

def general():
    # Collect Numbers
    numbers = []
    quantity = 3
    for i in range(0,quantity):
        number = int(input(f"enter the {i + 1} number: "))
        numbers.append(number)

    # Organize them
    numbersInSequence = []
    round = 1
    while(len(numbers) > 0):
        # start
        lowest = numbers[0]
        lowestId = 0 

        print(f"\n ROUND {round}")
        print(f"lowest: {lowest}")

        # Compare all the others
        for i in range(1, len(numbers)):
            if(numbers[i] < lowest):
                lowest = numbers[i]
                lowestId = i
            print(f"lowest: {lowest}")
            
        numbersInSequence.append(lowest)
        numbers.pop(lowestId)
        round += 1
            
    print(numbersInSequence)    

n1 = int(input("insira o numero 1: "))
n2 = int(input("insira o numero 2: "))
n3 = int(input("insira o numero 3: "))

if(n1 < n2 and n1 < n3 and n2 < n3):
    print(f"{n1}, {n2}, {n3}")

if(n1 < n2 and n1 < n3 and n3 < n2):
    print(f"{n1}, {n3}, {n2}")

if(n2 < n1 and n2 < n3 and n1 < n3):
    print(f"{n2}, {n1}, {n3}")

if(n2 < n1 and n2 < n3 and n3 < n1):
    print(f"{n2}, {n3}, {n1}")

if(n3 < n2 and n3 < n1 and n1 < n2):
    print(f"{n3}, {n1}, {n2}")

if(n3 < n2 and n3 < n1 and n2 < n1):
    print(f"{n3}, {n2}, {n1}")

