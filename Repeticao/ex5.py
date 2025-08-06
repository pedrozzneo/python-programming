""" Faça um programa que receba um número inteiro maior que 1,
verifique se o número é primo ou não e mostre a mensagem de
número primo ou de número não primo. Obs: Um número é primo
quando é divisível apenas por 1 e por ele mesmo. """

numero = int(input("insira um numero para verificar se eh primo ou nao: "))

divisor = 2
while(divisor < numero/2):
    if(numero % divisor == 0):
        print("nao eh primo")
        exit()
    divisor += 1

print("eh primo")