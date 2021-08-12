'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep


v1 = int(input('Primeiro Valor: '))
v2 = int(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        s = v1 + v2
        print('A soma entre {} + {} é {}'.format(v1, v2, s))
        print('=-=' * 10)
    elif opcao == 2:
        mul = v1 * v2
        print('O resultado de  {} x {} é {}'.format(v1, v2, mul))
        print('=-=' * 10)
    elif opcao == 3:
        if v1 > v2:
            print('Entre {} e {} o maior é {}'.format(v1, v2, v1))
            print('=-=' * 10)
        elif v2 > v1:
            print('Entre {} e {} o maior é {}'.format(v1, v2, v2))
            print('=-=' * 10)
        elif v1 == v2:
            print('Entre {} e {} são iguais'.format(v1, v2))
            print('=-=' * 10)
    elif opcao == 4:
        print('Informe os números novamente:')
        v1 = int(input('Primeiro Valor: '))
        v2 = int(input('Segundo valor: '))
        print('=-=' * 10)
    elif opcao == 5:
        print('Finalizando...')
        print('=-=' * 10)
        sleep(1)
        print('Fim do programa! Volte sempre!')
    else:
        print('Opção inválida. Tente novamente')
        print('=-=' * 10)
