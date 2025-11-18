"""Faça um programa que simule um jogo da loto. O computador deve gerar 5
números aleatoriamente entre 50 possíveis (0 a 49), armazenando as dezenas
sorteadas em um vetor (dez_sort) de 5 posições. Em seguida, o usuário deverá ler
uma lista com 10 posições, representando a aposta (conforme o exemplo abaixo).
O programa deve, então, verificar e imprimir uma mensagem mostrando quantos
números o usuário acertou. De acordo com o exemplo abaixo o usuário acertou 4
dezenas.
Exemplo:
dez_sort 10 15 21 23 49
aposta 1 5 10 12 15 17 23 31 42 49"""

import random

def sorteiaNumeros(quantidadeSorteados):
    dez_sort = []
    for i in range(quantidadeSorteados):
        numero = geraNumeroAleatorioDistinto(dez_sort)
        dez_sort.append(numero)
    return dez_sort

def geraNumeroAleatorioDistinto(lista):
    repetido = True # So para entrar no while a primeira vez
    while repetido:
        numero = random.randint(0, 49)
        repetido = False

        for i in range(len(lista)):
            if numero == lista[i]:
                repetido = True
                break
    return numero

def recebeNumeroDistinto(lista):
    repetido = True # So para entrar no while a primeira vez
    while repetido:
        numero = int(input())
        repetido = False

        for i in range(len(lista)):
            if numero == lista[i]:
                repetido = True
                print("esse numero ja foi apostado, insira outro: ", end = "")
                break
    return numero

def recebeApostas(quantidadeApostas):
    apostas = []
    for i in range(quantidadeApostas):
        numero = 50 # So para entrar no while a primeira vez
        while numero > 49 or numero < 0:
            print(f"aposta {i + 1}: ", end = "")
            numero = recebeNumeroDistinto(apostas)
            if numero > 49 or numero < 0:
                print("O número N respeita 0 <= N <= 49 ")
        # Adiciona na lista de apostas
        apostas.append(numero)
    print()
    return apostas

def contaAcertos(apostas, dez_sort):
    acertos = 0
    for i in range(10):
        for j in range(5):
            if apostas[i] == dez_sort[j]:
                acertos += 1
                break
    return acertos

def exibeLista(lista):
    for i in range(len(lista)):
        print(f"{lista[i]}", end = " ")
    print()

def main():
    quantidadeSorteados = 5
    dez_sort = sorteiaNumeros(quantidadeSorteados)

    # Lê as 10 apostas
    quantidadeApostas = 10
    apostas = recebeApostas(quantidadeApostas)

    # Conta a quantidade de acertos
    acertos = contaAcertos(apostas, dez_sort)
            
    print(f"Dezenas: ", end = "") 
    exibeLista(dez_sort)

    print(f"Apostas: ", end = "") 
    exibeLista(apostas)  

    print(f"Acertos: {acertos}")
main()
    

    