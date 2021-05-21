from time import sleep


def contador(x=0, y=0, z=1):
    print('-=' * 20)
    if z == 0:
        z = 1
    if x < 0 and y > 0 and z < 0:
        z *= -1
    if z > 0:
        print(f'Contagem de {x} até {y} de {z} em {z}', flush=True)
    else:
        print(f'Contagem de {x} até {y} de {z * -1} em {z * -1}', flush=True)
    sleep(2)
    for c in range(x, y + 1, z):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
