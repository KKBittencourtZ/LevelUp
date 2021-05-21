def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('NÃO VOTA')
    elif 18 > idade >= 16 or idade >= 70:
        print('VOTO É FACULTATIVO')
    else:
        print('VOTO É OBRIGATÓRIO')


nasc = int(input('Em que ano você nasceu? '))
voto(nasc)
