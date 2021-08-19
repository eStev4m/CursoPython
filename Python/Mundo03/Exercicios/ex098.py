'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''


from time import sleep


def contagem(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('\033[32m-=\033[m' * 24)
    sleep(0.5)
    print(f'\033[31mContagem de {i} até {f} de {p} em {p}\033[m')
    sleep(1)
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p
            sleep(0.5)
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            cont -= p
            sleep(0.5)
        print('FIM!')


# Programa Principal
contagem(1, 10, 1)
contagem(10, 0, 2)
print('\033[32m-=\033[m' * 24)
print('\033[1;33mAgora é sua vez de personalizar a contagem!\033[m')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
