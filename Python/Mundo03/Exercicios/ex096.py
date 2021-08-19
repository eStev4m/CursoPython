'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def área(lar, com):
    quad = lar * com
    print(f'A área do terreno {lar:.1f}x{com:.1f} é de {quad:.1f}m².')
    print()


# Programa Principal
print('  Controle de Terrenos')
print('-' * 20)
área(lar = float(input('LARGURA (m): ')), 
     com = float(input('COMPRIMENTO (m): ')))
