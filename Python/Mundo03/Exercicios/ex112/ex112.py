'''Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.'''

import utilidadesCeV.moeda
import utilidadesCeV.dado


valor = utilidadesCeV.dado.leiaDinheiro('Digite o preço: R$ ')
utilidadesCeV.moeda.resumo(valor)
print()
