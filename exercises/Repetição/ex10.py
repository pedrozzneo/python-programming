""""Calcular e escrever o valor do número , com precisão de 0.0001, usando a
série 4 - 4/3 + 4/5 - 4/7 + 4/9 ..."""

numerador = 4
denominador = 1
contador = 0
soma = 0

while contador < 10000:
    if(contador % 2 == 0):
        soma += numerador/denominador
    else:
        soma -= numerador/denominador

    denominador += 2
    contador += 1

print(f"pi: {soma:.4f}")