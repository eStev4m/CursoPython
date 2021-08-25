def aumentar(v = 0):
    val = v * (10/100) + v
    return val


def diminuir(v = 0):
    val = v - v * (10/100)
    return val


def dobro(v = 0):
    val = v * 2
    return val


def metade(v = 0):
    val = v / 2
    return val


def moeda(m):
    val = (f'R$ {m:5.2f}'.replace('.', ','))
    return val
