lanches = ('Hamburguer', 'Suco', 'Sorvete', 'Pizza')

# exemplo 1:
print(lanches[:2])
print(lanches[0])
print(lanches[-1])
print(lanches)
print(' ')

# exemplo 2:
for c in lanches:
    print(c)
print(' ')

#exemplo 3:
for comida in lanches:
    print(f'Eu comi essa comida {comida}.')
print(' ')

#exemplo 4:
for cont in range(0, len(lanches)):
    print(lanches[cont])
print(' ')

#exemplo 5:
for pos, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posição {pos + 1}')
print(' ')

#exemplo 6:
print(sorted(lanches))
print(' ')
