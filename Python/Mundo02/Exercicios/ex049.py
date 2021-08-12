# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{:2} x {:2} = \033[1;32m{:2}\033[m' .format(n, c, n * c))
