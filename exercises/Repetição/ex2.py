""""Faça um programa que imprima os 20 primeiros números primos"""

numero = 1

while numero <= 20:
    # Assumir a princípio que é primo uma vez que as condiçoes jogam pro outro lado, se elas nao forem satisfeitas, entao realmente é primo
    primo = True
    
    # Começar pelo 2 já que ser divisível por 1 não é determinante
    divisor = 2

    # Não há necessidade de verificar divisores maior que numero/2 pois a divisao com certeza da quebrada ou o próprio número (nao determinante)
    while divisor <= (numero/2):
        if(numero % divisor == 0):
            primo = False
            break
        
        divisor += 1 
    
    if primo:
        print(f"{numero} é primo")

    # Proximo numero
    numero += 1
