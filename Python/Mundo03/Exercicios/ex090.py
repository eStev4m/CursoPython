'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

classe = {}

classe['Nome'] = str(input('Nome: '))
classe['Média'] = float(input(f'Média de {classe["Nome"]}: '))
if classe['Média'] >= 7:
    classe['Situação'] = 'Aprovado'
elif 5 <= classe['Média'] < 7:
    classe['Situação'] = 'Recuperação'
else:
    classe['Situação'] = 'Reprovado'
print('-=' * 20)
for k, v in classe.items():
    print(f' - {k} é igual a {v}')
