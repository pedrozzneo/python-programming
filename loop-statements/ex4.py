""" Faça um programa para mostrar as tabuadas de todos os números de 1
a 10. """

numero = 1
while(numero < 10):
    print(f"\n\nTabuada do {numero}")
    for i in range(0, 10):
        print(f"{i+1} x {numero} = {numero * (i+1)}")
    numero += 1