times = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG',
        'Bahia', 'Ceará SC', 'Chapecoense', 'Corinthians', 'Cuiabá',
        'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional',
        'Juventude', 'Palmeiras', 'Bragantino', 'Santos', 'Sport Recife',
        'São Paulo')
print(f'Lista de times do Brasileirão: {times}')
print(f'Os 5 primeiros são {times[:5]}')
print(f'Os 4 últimos são {times[16:]}')
print(f'Times em ordem alfabética: {times}')
print(f'O Chapecoense está {times.index("Chapecoense") + 1}ª posição.')
