"""Crie um programa que leia inicialmente uma sequência de N númerosinteiros fornecidos pelo usuário e mostre ao final da leitura a sequênciaoriginal e a sequência invertida"""

QntdNumeros = int(input("elementos: "))

numeros = []
for i in range(QntdNumeros):
    numeros.append(int(input(f"valor do {i + 1} elemento: ")))
print(numeros)

reversed = []
for i in range(QntdNumeros-1, -1, -1):
    reversed.append(numeros[i])
print(reversed)

reversed = []
i = QntdNumeros-1
while i >= 0:
    reversed.append(numeros[i])
    i -= 1
print(reversed)