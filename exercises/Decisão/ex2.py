"""- Dois amigos, Alice e Bob, estão jogando um jogo muito simples, em
que um deles grita ou "par" ou "ímpar" e o outro imediatamente
responde ao contrário, respectivamente "ímpar" ou "par". Em seguida,
ambos exibem ao mesmo tempo uma mão cada um, em que alguns
dedos estão estendidos e outros dobrados. Então eles contam o número
total de dedos estendidos. Se a soma for par, quem gritou "par" ganha.
Se a soma for ímpar, quem gritou "ímpar" ganha. Por exemplo,
suponhamos que a Alice gritou "par" e o Bob respondeu "ímpar". Em
seguida, Alice não deixou nenhum dos seus dedos estendidos, ao passo
que Bob deixou três dedos estendidos. A soma então é três, que é ímpar,
portanto Bob ganhou. Seu programa deve determinar quem ganhou,
tendo a informação de quem gritou par e o número de dedos estendidos
de cada um.
Entrada
A entrada contém três linhas, cada uma com um número inteiro, P, D_1
e D_2, nesta ordem. Se P = 0 então Alice gritou "par", ao passo que se
P=1 então Bob gritou "par". Os números D_1 e D_2 indicam,
respectivamente, o número de dedos estendidos da Alice e do Bob.
Saída
Seu programa deverá imprimir uma única linha, contendo um único
número inteiro, que deve ser 0 se Alice foi a ganhadora, ou 1 se Bob foi
o ganhador.
Restrições
 P = 0 ou P = 1
 0 ≤ D_1 ≤ 5
 0 ≤ D_2 ≤ 5"""

P = int(input("qual o P?: \n - 0: Alice par e Bob impar \n - 1: Alice impar e Bob par \nR: "))
if(P != 0 and P != 1):
    print("entrada invalida ")
    exit()

D1 = int(input("D1: "))
if(D1 < 0 or D1 > 5):
    print("entrada invalida ")
    exit()

D2 = int(input("D2: "))
if(D2 < 0 or D2 > 5):
    print("entrada invalida ")
    exit()
    
soma = D1 + D2

# Soma par
if(soma % 2 == 0):
    print("Soma par!!")
    if(P == 0):
        print("Alice ganhou")
    elif(P == 1):
        print("Bob ganhou")

# Soma impar
else:
    print("Soma impar")
    if(P == 1):
        print("Alice ganhou")
    elif(P == 0):
        print("Bob ganhou")
