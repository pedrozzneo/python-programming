"""Faça uma função InteiroPositivo(n) que verifica se uma string fornecida como
parâmetro pode ser convertida para um número inteiro positivo. A função deverá
retornar True em caso afirmativo e False, caso contrário. O programa principal deverá
fazer a conversão para inteiro, caso o resultado da função seja True, ou imprimir a
mensagem adequada, caso o resultado seja False."""

def inteiroPositivo(entrada):
    try:
        if int(entrada) >= 0:
            return True
    except:
        return False

def main():
    entrada = input("entrada: ")

    if inteiroPositivo(entrada):
        print("é um inteiro positivo")
        entrada = int(entrada)
    else:
        print("NÃO é um inteiro positivo")

if __name__ == "__main__":
    main()