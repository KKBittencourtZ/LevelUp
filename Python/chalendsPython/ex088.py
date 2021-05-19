
from random import randint
print('-' * 35)
print(f'{"JOGA NA MEGA SENA":^35}')
print('-' * 35)
x = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {x} JOGOS -=-=-=')
números = []
for c in range(1, x + 1):
    print(f'Jogo {c}: ', end='')
    while len(números) != 6:
        roleta = randint(1, 60)
        if roleta not in números:
            números.append(roleta)
    números.sort()
    print(números)
    números.clear()
print('-=' * 20)
