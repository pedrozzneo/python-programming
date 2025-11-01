"""Faça uma função Real(n) que verifica se uma string fornecida como parâmetro pode
ser convertida para um número real. A função deverá retornar True em caso
afirmativo e False, caso contrário. O programa principal deverá fazer a conversão para
inteiro, caso o resultado da função seja True, ou imprimir a mensagem adequada,
caso o resultado seja False."""

def real(entrada):
    if entrada[0] == "-":
        try:
            float(entrada[1:])
            return True
        except:
            return False
    else:
        try:
            float(entrada)
            return True
        except:
            return False

def main():
    entrada = input("entrada: ")
    if real(entrada):
        entrada = (float(entrada[1:])) * -1
        print(f"{entrada} {type(entrada)}")
    else:
        print("NÃO da pra converter pra inteiro")

if __name__ == "__main__":
    main()
