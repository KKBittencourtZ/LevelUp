def leiaint(v):
    valor = input(v)
    while True:
        if valor.isnumeric():
            valor = valor
            break
        elif valor.isalpha() or valor.isspace() or valor.isalnum() or valor.isprintable():
            print('Erro, digite um número!')
            valor = str(input(v))
    return valor


# principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')


# Resolução do professor
'''
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um número inteiro válido.')
        if ok:
            break
    return valor

'''