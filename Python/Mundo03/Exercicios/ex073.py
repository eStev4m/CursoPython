'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Athletico-PR', 'Ceará SC',
'Santos', 'Atlético-GO', 'Bahia', 'Internacional', 'Corinthians', 'Fluminense', 'Juventude',
'Sport Recife', 'São Paulo', 'América-MG', 'Cuiabá', 'Grêmio', 'Chapecoense')

print('-=' * 70)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 70)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 70)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 70)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 70)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
print('-=' * 70)
