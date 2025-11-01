"""Crie uma função que receba como parâmetro um número inteiro. A função
deve retornar um número inteiro, conforme a seguir:
a) Retornar 1 se o número recebido é positivo
b) Retornar -1 se o número recebido é negativo
c) Retornar 0 se o número recebido é zero"""

def tratarInteiro(inteiro):
    if inteiro > 0:
        print("1")
        return 1
    elif inteiro < 0:
        print("-1")
        return -1
    else:
        print("0")
        return 0
    
inteiro = int(input("inteiro: "))
tratarInteiro(inteiro)
