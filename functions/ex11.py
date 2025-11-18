"""Faça uma função que receba 2 strings e retorne Verdadeiro se a
segunda string é um anagrama da primeira, ou Falso caso contrário."""

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

def anagrama(palavra1, palavra2):
    caracteresPalavra1 = {}                                           
    caracteresPalavra2 = {}

    caracteresPalavra1 = montaDict(palavra1, caracteresPalavra1)
    caracteresPalavra2 = montaDict(palavra2, caracteresPalavra2)

    if caracteresPalavra1 == caracteresPalavra2:
        return True
    else:
        return False                                

palavra1 = input("Palavra 1: ")                                           
palavra2 = input("Palavra 2: ") 

if anagrama(palavra1, palavra2):
    print("é anagrama")
else:
    print("nao é anagrama")
