'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS:
- considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('\033[32m=\033[m' * 40)
print('\033[1;33m{: ^40}\033[m'.format('BANCO ESTEVAM'))
print('\033[32m=\033[m' * 40)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
    
print('\033[32m=\033[m' * 40)
print('\033[35mVolte sempre ao BANCO ESTEVAM!\nTenha um bom dia!\033[m')