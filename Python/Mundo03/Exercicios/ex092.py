'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''


from datetime import date


cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
ano = int(input('Ano e Nascimento: '))
cadastro['Idade'] = date.today().year - ano
cadastro['CLT'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['CLT'] != 0:
    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Contratação'] + 35) - date.today().year)
    cadastro['Salário'] = (f'{float(input("Salário: R$ ")):.2f}')
print('-=' * 30)
for k, v in cadastro.items():
    print(f' - {k} tem o valor {v}')
print()
