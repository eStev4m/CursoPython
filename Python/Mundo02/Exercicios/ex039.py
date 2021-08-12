'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou
que passou do prazo.'''

from datetime import date


nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, date.today().year))
tempo = 18 - idade
alistamento = date.today().year + tempo

if idade <= 17:
    print('Ainda faltam {} ano(s) para o alistamento.\nSeu alistamento será em {}.'.format(tempo, alistamento))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Você já deveria ter se alistado há {} ano(s).\nSeu alistamento foi em {}.'.format(-tempo, alistamento))
