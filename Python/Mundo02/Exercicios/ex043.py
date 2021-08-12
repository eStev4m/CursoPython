'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

peso = float(input('Qual é seu peso? (Kg) '))
alt = float(input('Qual é sua altura? (m) '))
imc = peso / (alt * alt)
print('O IMC dessa pessoa é de {:.1f} kg/m2'.format(imc))

if imc <= 18.5:
    print('Abaixo do Peso')
elif 25 >= imc >= 18.4:
    print('Peso Ideal')
elif 30 >= imc >= 24.9:
    print('Sobrepeso')
elif 40 >= imc >= 29.9:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
