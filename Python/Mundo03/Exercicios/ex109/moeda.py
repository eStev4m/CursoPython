def aumentar(v = 0, formato = False):
    val = v * (10/100) + v
    return val if format is False else moeda(val)


def diminuir(v = 0, formato = False):
    val = v - v * (10/100)
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
