# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Uma distância em metros: '))
print('A medida de {:.1f}m corresponde a' .format(metros))
print('{}km' .format(metros/1000))
print('{}hm' .format(metros/100))
print('{}dam' .format(metros/10))
print('{:.0f}dm' .format(metros*10))
print('{:.0f}cm' .format(metros*100))
print('{:.0f}mm' .format(metros*1000))
