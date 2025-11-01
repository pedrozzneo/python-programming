"""Faça um programa que simule uma calculadora. Ou seja, o programa
deve apresentar para o usuário um menu de opções conforme o
exemplo a seguir. O usuário deverá escolher a opção desejada,
fornecer as entradas necessárias e o programa irá calcular e
apresentar o resultado na tela. Obs: utilize as funções pré-definidas
na biblioteca math."""
import math

def menu():
    opcao = 0
    while opcao < 1 or opcao > 8:
        print("\nOpções:")
        print("1: raíz quadrada")
        print("2: cosseno")
        print("3: seno")
        print("4: tangente")
        print("5: fatorial")
        print("6: log natural")
        print("7: log2")
        print("8: sair\n")

        opcao = int(input("Escolha: "))

        if opcao < 1 or opcao > 8:
            print("entrada inválida!!")
        else:
            return opcao
        
def main():
    opcao = 1
    while opcao != 8:
        opcao = menu()

        if opcao == 1:
            operando = int(input("numero: "))
            print(f"raiz quadrada de {operando}: {math.sqrt(operando)}")
        elif opcao == 2:
            operando = int(input("numero: "))
            print(f"cosseno de {operando}: {math.cos(operando)}")
        elif opcao == 3:
            operando = int(input("numero: "))
            print(f"seno de {operando}: {math.sin(operando)}")
        elif opcao == 4:
            operando = int(input("numero: "))
            print(f"tangente de {operando}: {math.tan(operando)}")
        elif opcao == 5:
            operando = int(input("numero: "))
            print(f"fatorial de {operando}: {math.factorial(operando)}")
        elif opcao == 6:
            operando = int(input("numero: "))
            print(f"log de {operando}: {math.log(operando)}") 
        elif opcao == 7:
            operando = int(input("numero: "))
            print(f"log2 de {operando}: {math.log2(operando)}")
        elif opcao == 8:
            print("Muito obrigado!!")
main()