'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''

print('=' * 10, 'LOJAS ESTEVAM', '=' * 10)
preco = float(input('Preço das compras: R$ '))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2X no cartão
[ 4 ] 3X ou mais no cartão''')
opcao = int(input('Qual é a sua opção? '))
if opcao == 1:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, preco - (preco * 10/100)))
elif opcao == 2:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, preco - (preco * 5/100)))
elif opcao == 3:
    print('Sua compra de R$ {:.2f} será parcelada em 2X de R$ {:.2f} SEM JUROS.'.format(preco, preco / 2))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('''Sua compra será parcelada em {}X de R$ {:.2f} COM JUROS.
Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'''.format(parcelas, (preco / parcelas) + ((preco / parcelas) * 20/100) , preco, preco + (preco * 20/100)))
else:
    print('Opção não existente!\nTente as opções válidas!')
