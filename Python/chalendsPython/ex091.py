from random import randint
from time import sleep
play = {}
stok = []
final = []
gabarito = []
print('Valores sorteados: ')
sleep(1)
for c in range(1, 5):
    play['player'] = str(f'{c}º jogador')
    play['dado'] = randint(1, 6)
    stok.append(play.copy())
    gabarito.append(play['dado'])
    print(f'{play["player"]} tirou {play["dado"]} no dado.')
    sleep(0.5)
    play.clear()
print('=' * 15)
gabarito.sort()
gabarito.reverse()
print('  == RANKING DOS JOGADORES ==')
while len(final) != 4:
    for c in range(0, 4):
        if stok[c]['dado'] == gabarito[0]:
            final.append(stok[c])
            gabarito.remove(gabarito[0])
            if len(gabarito) == 0:
                break
for n, r in enumerate(final):
    print(f'   {n + 1}º lugar: {final[n]["player"]} com {final[n]["dado"]}')
    sleep(0.5)

#Solução do professor
'''
from random import randint
from operator import itemgetter
jogo = {'jogador1': randint, ...}
ranking = []
print('valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')

'''