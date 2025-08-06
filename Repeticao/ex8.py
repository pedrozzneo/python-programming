""" Faça um programa que mostre os 8 primeiros termos da sequência de
Fibonacci. Ex: 0, 1, 1, 2, 3, 5, 8,13, 21,34, 55..."""

anterior = 0
atual = 1
print(anterior)
print(atual)

contador = 0
while(contador < 6):
    # Exibir proximo numero
    print(anterior + atual) 

    # Preparar para a proxima iteracao
    anterior = atual
    atual = anterior + atual
    contador += 1