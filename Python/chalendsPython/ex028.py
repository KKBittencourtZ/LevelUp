from math import e
from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
robo = randint(0, 5)
player = int(input('Em que número eu pensei? '))
sleep(1)
print('PROCESSANDO...')
sleep(1)
if robo == player:
    print('PARABÉNS !!! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {robo} e não no {player}!')
