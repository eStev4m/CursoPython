'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras =('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
            'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
            'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')
for pal in palavras:
    print(f'\nNa palavra \033[1;34m{pal}\033[m temos ', end='')
    for letra in pal:
        if letra.upper() in 'AEIOU':
            print(f'\033[1;33m{letra}\033[m', end=' ')
