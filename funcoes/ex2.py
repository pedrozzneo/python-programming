"""Faça uma função Inteiro(n) que verifica se uma string fornecida como parâmetro
pode ser convertida para um número inteiro positivo ou negativo. A função deverá
retornar True em caso afirmativo e False, caso contrário. O programa principal deverá
fazer a conversão para inteiro, caso o resultado da função seja True, ou imprimir a
mensagem adequada, caso o resultado seja False."""

def inteiro(entrada):
    if entrada[0] == "-":
        try:
            int(entrada[1:])
            return True
        except:
            return False
    else:
        try:
            int(entrada)
            return True
        except:
            return False

entrada = input("entrada: ")

if inteiro(entrada):
    entrada = (int(entrada[1:])) - 1
    print(f"{entrada} {type(entrada)}")
else:
    print("NÃO da pra converter pra inteiro")