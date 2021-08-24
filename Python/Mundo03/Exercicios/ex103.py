'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''

def ficha():
    print('-' * 30)
    jog = str(input('Nome do Jogador: ')).strip()
    if jog == '':
        jog = '<DESCONHECIDO>'
    gol = str(input('Números de Gols: '))
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    print(f'O jogdor {jog} fez {gol} gol(s) no campeonato.')


# Programa Principal
ficha()
