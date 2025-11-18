"""Função recursiva que exibe uma string na ordem
inversa."""

# Função que retorna a string invertida
def reverse_string(string, index):
    if index == 0:
        return string[index]
    else:
        return string[index] + reverse_string(string, index-1)
    
def main():
    # Entrada da string
    string = input("string para inverter: ")

    # Exibição da string invertida
    print(f"string invertida: {reverse_string(string, len(string)-1)}")
main()