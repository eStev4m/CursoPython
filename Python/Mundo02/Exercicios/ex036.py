'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''


vc = float(input('Valor da casa: R$ '))
sc = float(input('Salário do comprador: R$ '))
af = int(input('Quantos anos de financiamento: '))
pres = vc / (af * 12)
minimo = sc * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}' .format(vc, af, pres))
if pres <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo negado!')
