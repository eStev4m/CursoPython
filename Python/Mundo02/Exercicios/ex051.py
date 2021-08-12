# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 30)
print('{:>5}'.format('10 TERMOS DE UMA P.A.'))
print('=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (11 - 1) * razao

for c in range(termo, decimo, razao):
    print(c, end=' -> ')
print('ACABOU!')
