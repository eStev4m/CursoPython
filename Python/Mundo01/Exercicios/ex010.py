# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

r = float(input('Quanto dinheiro você tem na carteira? R$ '))
# valor do dollar em 03-08-2021
d = r / 5.20
print('Com R$ {:.2f} você pode comprar US$ {:.2f}' .format(r, d))
