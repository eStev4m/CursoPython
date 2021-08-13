'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

valor = []
for pos in range(0, 5):
    valor.append(int(input(f'Digite um valor para a Posição {pos}: ')))
print('=-' * 30)
print(f'Você digitou os valores {valor}')
maior = max(valor)
menor = min(valor)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i}... ')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i}... ')
print()
