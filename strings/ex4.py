"""Escreva um programa que reconhece se uma string é um palíndromo.
Exemplo: arara, ovo, reter."""

palavra = (input("insira uma palavra para eu analisar se é ou não palíndromo: ")).lower()
palindromo = True

palavra = palavra.replace(" ", "")
palavra = palavra.replace("-" , "")
palavra = palavra.replace(",", "")
palavra = palavra.replace("ô", "o")

print(palavra)

# i é o índice do começo que vai para frente e j do final que vai para trás
i = 0
j = -1 
while i < len(palavra) and palindromo:
    # Condição que não é palíndromo
    if palavra[i] != palavra[j]:
        palindromo = False
        print(i, j)
        print(palavra[i], palavra[j])
    
    # Preparar para os próximos iniciais e finais
    i += 1
    j -= 1

if palindromo:
    print("é palindromo")
else:
    print("nao é palindromo")