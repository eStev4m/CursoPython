'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''


num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('''[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} conertido para BINÁRIO é igual a {}' .format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} conertido para OCTAL é igual a {}' .format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} conertido para HEXADECIMAL é igual a {}' .format(num, hex(num)[2:]))
else:
    print('Esse número não está na opção, tente de novo!')
