print('Gerador de PA')
print('-=' * 8)
termo1 = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
cont = 0
pa = termo1
while cont != 10:
    print(pa, end=' -> ')
    pa += razão
    cont += 1
print('FIM')
