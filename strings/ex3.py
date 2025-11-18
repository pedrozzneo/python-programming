"""Escreva um programa que verifique se duas strings fornecidas pelo
usuário são iguais e mostre o total de caracteres de cada uma delas.
Diferencie letras maiúsculas das minúsculas."""

string1 = input("string 1:")
string2 = input("string 2:")

print(f"\ntamanho da primeira: {len(string1)}")
print(f"tamanho da segunda: {len(string2)}")

iguais = False
if string1 == string2:
    print(f"As strings possuem o mesmo conteúdo")
else:
    print(f"As strings possuem conteúdo diferente")