'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
j = int(input('Em que número eu pensei? '))

sleep(2)
print('PROCESSANDO...')

c = randint(0, 5)

sleep(3)
if j == c:
    print('PARABÉNS! Você  conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!' .format(c, j))
