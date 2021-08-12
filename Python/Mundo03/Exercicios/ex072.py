'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
'Dezenove', 'Vinte')
while True:
    digite = int(input('Digite um número entre 0 e 20: '))
    if 0 <= digite <= 20:
        break
    else:
        print('Tente novamente.', end=' ')
print(f'Você digitou o número {numeros[digite]}')
