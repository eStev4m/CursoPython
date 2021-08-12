'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando \033[1;4;36m{:.1f}\033[m e \033[1;4;36m{:.1f}\033[m, a média do aluno é \033[1;4;34m{:.1f}\033[m'.format(n1, n2, media))

if media >= 7:
    print('O aluno está \033[1;4;36mAPROVADO\033[m.')
elif media >= 5 and media <= 6.9:
    print('O aluno está de \033[1;4;33mRECUPERAÇÃO\033[m.')
else:
    print('O aluno está \033[1;4;31mREAPROVADO\033[m.')
