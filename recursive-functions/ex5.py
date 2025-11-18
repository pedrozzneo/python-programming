"""Escreva um algoritmo recursivo para retornar
a quantidade de caracteres de uma string."""

# Função que retorna a quantidade de caracteres de uma string
def count_chars(string):
    if string == "":
        return 0
    else:
        return 1 + count_chars(string[1:])

def main():
    # Entrada da string
    string = input("string para contar caracteres: ")

    # Exibição da quantidade de caracteres
    print(f"'{string}' tem {count_chars(string)} caracteres.")
main()