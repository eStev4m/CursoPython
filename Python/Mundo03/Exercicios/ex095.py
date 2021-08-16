'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

campeonato = {}
gol = []
time = []

while True:
    campeonato.clear()
    campeonato['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {campeonato["Nome"]} jogou? '))
    gol.clear()
    for c in range(1, partidas + 1):
        gol.append(int(input(f'   Quantos gols na partida {c}? ')))
    campeonato['Gols'] = gol[:]
    campeonato['Total'] = sum(gol)
    time.append(campeonato.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in campeonato.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< Volte sempre! >>')
