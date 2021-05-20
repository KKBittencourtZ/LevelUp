jogador = {}
gols = []
total = 0
jogador['nome'] = str(input('Nome do jogador: '))
vezes = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, vezes):
    x = int(input(f' Quantos gols na partida {c + 1}? '))
    gols.append(x)
    total += x
jogador['gols'] = gols[:]
jogador['total'] = total
print('~ ' * 20)
print(jogador)
print('~ ' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('~ ' * 20)
print(f'O jogador {jogador["nome"]} jogou {vezes} partidas.')
for c in range(0, vezes):
    print(f'  =>  Na partida {c + 1}, fez {jogador["gols"][c]} gols')
print(f'Foi um total de {jogador["total"]} gols.')
print('~ ' * 20)
