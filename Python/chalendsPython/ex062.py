print('Gerador de PA')
print('-=' * 8)
termo1 = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
cont = 0
pa = termo1
pausa = 10
while True:
    print(pa, end=' -> ')
    pa += razão
    cont += 1
    if cont == pausa:
        print('PAUSA')
        breakpoint
        mais = int(input('Quantos termos você quer mostrar a mais? '))
        if mais > 0:
            pausa += mais
        elif mais == 0:
            break
print(f'Progressão finalizada com {cont} termos mostrados.')
