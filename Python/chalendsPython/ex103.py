def ficha(jogador='<desconhecido>', gols=0):
    if jogador == '':
        jogador = '<desconhecido>'
    if gols == '':
        gols = '0'
    print(f'O jogador {jogador} fez {gols} gol(s) no cmapeonato.')
    
    
nome = str(input('Nome do jogador: ')).capitalize().strip()
g = str(input('Número de gols: '))
ficha(nome, g)
