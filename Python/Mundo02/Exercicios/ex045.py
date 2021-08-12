# Crie um programa que faça o computador jogar Jokenpô com você.


from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opcao = int(input('Qual é a sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[opcao]))
print('-=' * 12)
if computador == 0:
    if opcao == 0:
        print('EMPATE')
    elif opcao == 1:
        print('JOGADOR VENCE')
    elif opcao == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if opcao == 0:
        print('COMPUTADOR VENCE')
    elif opcao == 1:
        print('EMPATE')
    elif opcao == 2:
        print('JOGADOR VENCE')
    else:     
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if opcao == 0:
        print('JOGADOR VENCE')
    elif opcao == 1:
        print('COMPUTADOR VENCE')
    elif opcao == 2:
        print('EMPATE')
    else:     
        print('JOGADA INVÁLIDA!')
