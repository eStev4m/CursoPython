'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

cadastro = {}
fixa = []
soma = media = 0
while True:
    cadastro.clear()
    cadastro['Nome'] = str(input('Nome: ')).strip()
    while True:
        cadastro['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if cadastro['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    cadastro['Idade'] = int(input('Idade: '))
    soma += cadastro['Idade']
    fixa.append(cadastro.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(fixa)} pessoas cadastradas.')
media = soma / len(fixa)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in fixa:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in fixa:
    if p['Idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< Encerrado >>')
