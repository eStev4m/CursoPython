'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep


print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)

chances = []

qtd = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 2, f'SORTEANDO  {qtd}  JOGOS', '-=' * 2)
for jog in range(1, qtd + 1):
    numeros = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)]
    numeros.sort()
    chances.append(numeros[:])
    numeros.clear()
for i, c in enumerate(chances):
    sleep(1)
    print(f'Jogo {i + 1}: {c}')
print('-=' * 3, f'{"< BOA SORTE! >":^17}', '-=' * 3)
