"""Um anagrama é uma palavra que é feita a partir da transposição das
letras de outra palavra ou Palavra. Por exemplo, “Iracema” é um
anagrama para “America”. Escreva um programa que decida se uma
string é um anagrama de outra string, ignorando os espaços em branco.
O programa deve considerar maiúsculas e minúsculas como sendo
caracteres iguais, ou seja, “a” = “A”."""

# def removerLetraIndex(i, palavra):
#     if i+1 < len(palavra):
#         return palavra[:i] + palavra[i+1:]
#     return palavra[:i]

# def procuraCaracterPalavra(caracter, palavra):
#     for indice in range(len(palavra)):
#         if caracter == palavra[indice]:
#             return True, indice
#     return False, 0

# def solucao1():
#     palavra1 = (input("palavra 1:")).lower().replace(" ", "")
#     palavra2 = (input("palavra 2:")).lower().replace(" ", "")

#     if len(palavra1) == len(palavra2):
#         anagrama = True
#         while len(palavra1) != 0 and anagrama:
#             match, indice = procuraCaracterPalavra(palavra1[0], palavra2)
#             if not match:
#                 anagrama = False
#                 print("nao é anagrama") 
#             else:
#                 palavra1 = removerLetraIndex(0, palavra1)
#                 palavra2 = removerLetraIndex(indice, palavra2)
#         if anagrama:
#             print("é anagrama")
#     else:
#         print("nao é anagrama")

def contaCaracter(caracter, palavra):
    quantidade = 0
    for i in range(len(palavra)):
        if palavra[i] == caracter:
            quantidade += 1
    return quantidade

def montaDict(palavra, caracteresPalavra):
    for i in range(len(palavra)):
        if palavra[i] != " ":
            quantidade = contaCaracter(palavra[i], palavra)
            caracteresPalavra[palavra[i]] = quantidade
    return caracteresPalavra

def solucao2():
    palavra1 = input("Palavra 1: ")                                           
    palavra2 = input("Palavra 2: ")      
    caracteresPalavra1 = {}                                           
    caracteresPalavra2 = {}

    caracteresPalavra1 = montaDict(palavra1, caracteresPalavra1)
    caracteresPalavra2 = montaDict(palavra2, caracteresPalavra2)

    if caracteresPalavra1 == caracteresPalavra2:
        print("é anagrama")
    else:
        print("Não é anagrama")                                
solucao2()                