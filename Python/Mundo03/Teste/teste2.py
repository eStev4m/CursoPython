a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(f'A Tupla é {c}.')
print(' ')

# O exemplo esta mostrando quantas vezes irá aparecer o número 5
print(f'O 5 esta aparecendo {c.count(5)} vezes.')
print(' ')

# O exemplo esta mostrando em qual posição esta o número 8
print(f'O número 8 esta na posição {c.index(8)}.')
print(' ')

# Exemplo de número maior e número menor
print(f'Número maior: {max(c)}')
print(f'Número menor: {min(c)}')