""""Faça um programa que receba a idade de um eleitor e informa se o
voto dele é facultativo (entre 16 e 17 anos), obrigatório (entre 18 a 65),
se ele está dispensado de votar (acima de 65) ou ainda se ele não tem
idade para votar."""

age = int(input("enter your age: "))

if(age < 16):
    print("You can't vote")
elif(age <= 17):
    print("Your vote is optional")
elif(age <= 65):
    print("You HAVE to vote")
else:
    print("You don't have to vote")
