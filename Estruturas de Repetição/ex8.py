""" Faça um programa que mostre os 8 primeiros termos da sequência de
Fibonacci. Ex: 0, 1, 1, 2, 3, 5, 8,13, 21,34, 55..."""

anterior = 0
atual = 1
proximo = 1
contador = 0

print(anterior)
print(atual)
print(proximo)

while(contador < 8):
    # atualizar os novos valores
    anterior = atual
    atual = proximo
    proximo = anterior + atual 

    print(proximo) 

    # Preparar para a proxima iteracao
    contador += 1

