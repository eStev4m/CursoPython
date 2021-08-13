'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foramcadastradas.
B) Uma listagem com as pessoas mais pesadas. 
C) Uma listagem com as pessoas mais leves.'''

lista = []
cadastro = []
maior = menor = 0
while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = cadastro[1]
    else:
        if cadastro[1] > maior:
            maior = cadastro[1]
        if cadastro[1] < menor:
            menor = cadastro[1]
    lista.append(cadastro[:])
    cadastro.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()
