"""Crie um programa que dada uma sequência de N elementos fornecidospelo usuário mostre a sequência original e a sequência elevada ao cubo"""

QntdElementos = int(input("elementos: "))

elementos = []
for i in range(QntdElementos):
    elementos.append(int(input(f"valor do {i + 1} elemento: ")))
print(elementos)

for i in range(QntdElementos):
    elementos[i] **= 3
print(elementos)