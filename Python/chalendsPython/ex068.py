from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPEAR')
print('=-' * 20)
cont = 0
while True:
    pc = randint(1, 10)
    player = int(input('Diga um valor: '))
    parouimpar = ''
    while parouimpar not in 'PI':
        parouimpar = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    print('-' * 40)
    soma = pc + player
    imparoupar = "PAR" if soma % 2 == 0 else "ÍMPAR"
    print(f'Você jogou {player} e o computador {pc}. Total de {soma} é {imparoupar}')
    print('-' * 40)
    if parouimpar == imparoupar[0]:
        print('Você VENCEU !!!')
        print('Vamos jogar novamente...')
        cont += 1
    elif parouimpar != imparoupar[0]:
        print('Você PERDEU !!!')
        break
    print('=-' * 20)
print(f'GAME OVER! Você venceu {cont} vezes')
