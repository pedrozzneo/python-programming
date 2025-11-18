"""Crie uma função recursiva que exiba
verticalmente uma string"""

# Função que exibe verticalmente uma string
def exibir_vertical(string):
    if string == "":
        return
    print(string[0])
    exibir_vertical(string[1:])

def main():
    # Entrada da string
    string = input("string para exibir verticalmente: ")

    # Exibição vertical da string
    exibir_vertical(string)
main()
