# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
p = float(input('Primeiro segmento: '))
s = float(input('Segundo segmento: '))
t = float(input('Terceiro segmento: '))
if p < s + t and s < p + t and t < p + s:
    print('Os segmentos acima \033[1;34mPODEM FORMAR\033[m triângulo!')
else:
    print('Os segmentos acima \033[1;31mNÃO PODEM FORMAR\033[m triângulo!')
