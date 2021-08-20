'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


def voto(pes):
    from datetime import date
    pes = date.today().year - nasc
    if pes < 16:
        print(f'Com {pes} anos: Não Vota')
        return(pes)
    elif 16 <= pes < 18 or pes > 65:
        print(f'Com {pes} anos: Voto Opcional')
        return(pes)
    else:
        print(f'Com {pes} anos: Voto Obrigatório')
        return(pes)

print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
voto(nasc)
