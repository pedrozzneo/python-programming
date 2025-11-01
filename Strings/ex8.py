"""Dada uma string com uma frase informada pelo usuário (incluindo
espaços em branco), conte a quantidade de espaços em branco e a
quantidade de vezes que aparecem as vogais a, e, i, o, u."""

frase = input("frase: ")

Quantidade_a = 0
Quantidade_e = 0
Quantidade_i = 0
Quantidade_o = 0
Quantidade_u = 0
Quantidade_Brancos = 0

for i in range(len(frase)):
    if frase[i] == "a":
        Quantidade_a += 1
    elif frase[i] == "e":
        Quantidade_e += 1
    elif frase[i] == "i":
        Quantidade_i += 1
    elif frase[i] == "o":
        Quantidade_o += 1
    elif frase[i] == "u":
        Quantidade_u += 1
    elif frase[i] == " ":
        Quantidade_Brancos += 1

print(f"A palavra possui {Quantidade_a} letras a")
print(f"A palavra possui {Quantidade_e} letras e")
print(f"A palavra possui {Quantidade_i} letras i")
print(f"A palavra possui {Quantidade_o} letras o")
print(f"A palavra possui {Quantidade_u} letras u")
print(f"A palavra possui {Quantidade_Brancos} espaços em branco")