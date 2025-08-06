""" Faça um programa para mostrar a tabuada de um número qualquer
fornecido pelo usuário. Por exemplo, se o número fornecido for igual a
3, o programa de apresentar a seguinte saída:
Exercícios
1 x 3 = 3
2 x 3 = 6
3 x 3 = 9
4 x 3 = 12
5 x 3 = 15
6 x 3 = 18
7 x 3 = 21
8 x 3 = 24
9 x 3 = 27 """

numero = int(input("numero para tabuada: "))

contador = 1
while(contador < 10):
    print(f"{contador} x {numero} = {numero * (contador)}")
    contador += 1