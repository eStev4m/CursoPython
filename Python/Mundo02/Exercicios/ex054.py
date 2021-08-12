# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date


maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos \033[1;36m{}\033[m pessoa(s) maiore(s) de idade'.format(maior))
print('E também tivemos \033[1;32m{}\033[m pessoa(s) menore(s) de idade'.format(menor))
