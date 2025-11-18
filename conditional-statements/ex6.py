""""Uma determinada loja está fazendo promoções de vendas. Qualquer
compra que um cliente fizer até R$ 100,00 receberá 5% de desconto. Se
a compra for maior que R$ 100,00, mas inferior a R$ 200,00, o desconto
será de 10%. Se for superior ou igual a R$ 200,00, o desconto será de
20%.
Faça um programa que leia o quanto o cliente gastou e escreva o valor da
conta já com os descontos."""

price = float(input("price: "))

if(price <= 100):
    price *= 0.95
    
elif(price < 200):
    price *= 0.90

else:
    price *= 0.80

print(f" new price is: {price}")