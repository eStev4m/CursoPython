'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

primeiro = float(input('Primeiro segmento: '))
segundo = float(input('Segundo segmento: '))
terceiro = float(input('Terceiro segmento: '))

if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if primeiro == segundo == terceiro:
        print('\033[1;36mEQUILÁTERO!\033[m')
    elif primeiro != segundo != terceiro != primeiro:
        print('\033[1;33mESCALENO!\033[m')
    else: 
        print('\033[1;31mISÓSCELES!\033[m')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
