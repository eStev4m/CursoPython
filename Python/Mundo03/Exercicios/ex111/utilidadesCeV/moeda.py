def aumentar(v = 0, formato = False):
    val = v * (20/100) + v
    return val if format is False else moeda(val)


def diminuir(v = 0, formato = False):
    val = v - v * (12/100)
    return val if format is False else moeda(val)


def dobro(v = 0, formato = False):
    val = v * 2
    return val if format is False else moeda(val)


def metade(v = 0, formato = False):
    val = v / 2
    return val if format is False else moeda(val)


def moeda(m):
    val = (f'R$ {m:5.2f}'.replace('.', ','))
    return val


def resumo(r = 0):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(r)}')
    print(f'O dobro do preço: \t{dobro(r, True)}')
    print(f'Metade do preço: \t{metade(r, True)}')
    print(f'20% de aumento: \t{aumentar(r, True)}')
    print(f'12% de redução: \t{diminuir(r, True)}')
    print('-' * 35)
