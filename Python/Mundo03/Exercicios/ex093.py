'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

campeonato = {}
gol = []
campeonato['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {campeonato["Nome"]} jogou? '))
for g in range(1, partidas + 1):
    gol.append(int(input(f'   Quantos gols na partida {g}? ')))
campeonato['Gols'] = gol[:]
campeonato['Total'] = sum(gol)
print('-=' * 30)
print(f'{campeonato}')
print('-=' * 30)
for k, v in campeonato.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {campeonato["Nome"]} jogou {len(campeonato["Gols"])} partidas.')
for i, v in enumerate(campeonato['Gols']):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {campeonato["Total"]} gols.')
print('-=' * 30)
