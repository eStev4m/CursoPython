'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva(‘Olá, Mundo!’)
Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~'''


def escreva(msg):
    msgs = len(msg) + 4
    print('~' * msgs)
    print(f'  {msg}')
    print('~' * msgs)



# Programa Principal
escreva('Estevam Jannuzzi')
escreva('Curso de Python')
escreva('CeV')
