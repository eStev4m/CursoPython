'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''

import moeda

valor = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {valor:.2f} é R$ {moeda.metade(valor):.2f}')
print(f'O dobro de R$ {valor:.2f} é R$ {moeda.dobro(valor):.2f}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(valor):.2f}')
print(f'Diminuir 10%, temos R$ {moeda.diminuir(valor):.2f}')
print()
