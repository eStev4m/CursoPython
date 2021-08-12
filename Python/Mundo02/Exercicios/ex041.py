'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''

from datetime import date


nascimento = int(input('Ano do nascimento: '))
idade = date.today().year - nascimento

if idade <= 9:
    print('O atleta tem {} anos.\nClassificação: \033[1;36mMIRIM\033[m'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos.\nClassificação: \033[1;35mINFANTIL\033[m'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos.\nClassificação: \033[1;34mJÚNIOR\033[m'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos.\nClassificação: \033[1;33mSÊNIOR\033[m'.format(idade))
else:
    print('O atleta tem {} anos.\nClassificação: \033[1;32mMASTER\033[m'.format(idade))
