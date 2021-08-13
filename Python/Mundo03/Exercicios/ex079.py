'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

valor = []
while True:
    v = int(input('Digite um valor: '))
    if v not in valor:
        valor.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=' * 30)
valor.sort()
print(f'Você digitou os valores {valor}')
