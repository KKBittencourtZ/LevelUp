from random import randint


def roleta():
    global números
    números = []
    for c in range(0, 5):
        x = randint(1, 9)
        números.append(x)
    print('Sorteando 5 valores da lista: ', end='')
    for n in números:
        print(n, end=' ')
    print('PRONTO!')
def pares(list):
    somador = 0
    for n in list:
        if n % 2 == 0:
            somador += n
    print(f'Somando os valores pares de {números}, temos {somador}')
    


roleta()
pares(números)
