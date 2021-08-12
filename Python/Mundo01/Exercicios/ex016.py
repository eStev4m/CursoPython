'''Crie um programa que leia um número Real qualquer pelo
teclado e mostre na tela a sua porção Inteira.'''

import math

v = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(v, (math.trunc(v))))


from math import trunc

v = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(v, (trunc(v))))
