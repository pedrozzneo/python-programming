""""Faça um programa que gere aleatoriamente um número entre 0 e 100. Em seguida,
o programa deve pedir que o usuário tente acertar qual o número gerado. Por
exemplo, suponha que o programa gere o número 21 e o usuário tente adivinhálo digitando o número 50. O programa deve, então, imprimir a mensagem:
“Número incorreto, tente um valor menor”. O usuário digita, então, o número 10.
Após a análise deste número, o programa deverá imprimir a mensagem “Número
incorreto, tente um valor maior”. O processo deve continuar até que o usuário
acerte o número gerado pelo programa. O programa deve finalizar informando o
número de tentativas até o acerto.
Obs: use a função randint() para gerar o número aleatoriamente. """

import random

numeroAleatorio = random.randint(0, 100)
guess = -1

tentativas = 0
while guess != numeroAleatorio:
    tentativas += 1
    print(f"tentativa {tentativas}")

    if tentativas == 1:
        guess = int(input("adivinhe o valor do numero aleatório: "))

    elif guess < numeroAleatorio:
        guess = int(input("Numero incorreto, tente um valor maior: "))

    elif guess > numeroAleatorio:
       guess = int(input("Numero incorreto, tente um valor menor: "))

    

print(f"Parabens!! vc acertou o numero {numeroAleatorio} após {tentativas} tentativas!! ")