time = []
jogador = {}
gols = []
total = 0
while True:
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    vezes = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, vezes):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
        total += gols[c]
    jogador['gols'] = gols[:]
    jogador['total'] = total
    time.append(jogador.copy())
    pergunta = str(input('Quer continuar? ')).strip().upper()[0]
    while pergunta not in 'SN':
        print('ERRO! Apenas S ou N.')
        pergunta = str(input('Quer continuar? ')).strip().upper()[0]
    if pergunta == 'N':
        break
    gols.clear()
    total = 0
print('~ ' * 25)
print('cod  nome           gols         total')
print('--------------------------------------')
for w, e in enumerate(time):
    print(f' {w:2}  {e["Nome"]:<15}{e["gols"]} {e["total"]:>3}')
print('--------------------------------------')
while vezes != 999:
    vezes = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if vezes <= len(time) - 1:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[vezes]["Nome"]}:')
        for c in range(0, len(time[vezes]['gols'])):
            print(f'  => No jogo {c + 1} fez {time[vezes]["gols"][c]} gols.')
    if vezes == 999:
        print('Tchau Tchau ^^')
    else:
        print('Jogador não encontrado.')

# Solução para a tabela do professor:
'''

for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()

'''