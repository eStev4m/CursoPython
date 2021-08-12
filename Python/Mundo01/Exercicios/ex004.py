#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

d = input('Digite algo: ')
print('O tipo de primitivo desse valor é {}' .format(type(d)))
print('Só tem espaços? {}' .format(d.isspace()))
print('É um número? {}' .format(d.isnumeric()))
print('É alfabético? {}' .format(d.isalpha()))
print('É alfanumérico? {}' .format(d.isalnum()))
print('Está em maiúsculas? {}' .format(d.isupper()))
print('Está em minúsculas? {}' .format(d.islower()))
print('Está capitilizada? {}' .format(d.istitle()))
