from random import randint
from time import sleep
lista =['PEDRA', 'PAPEL', 'TESOURA']
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
pc = randint(0, 2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-=' * 10)
print(f'COMPUTADOR jogou {lista[pc]}')
print(f'Jogador jogou {lista[jogador]}')
print('-=' * 10)
if jogador == 0:
    if pc == 0:
        print('EMPATE')
    elif pc == 1:
        print('COMPUTADOR VENCE')
    elif pc == 2:
        print('JOGADOR VENCE')
elif jogador == 1:
    if pc == 0:
        print('JOGADOR VENDE')
    elif pc == 1:
        print('EMPATE')
    elif pc == 2:
        print('COMPUTADOR VENCE')
elif jogador == 2:
    if pc == 0:
        print('COMPUTADOR VENCE')
    elif pc == 1:
        print('JOGADOR VENCE')
    elif pc == 2:
        print('EMPATE')
else:
    print('OPÇÃO INVÁLIDA')
