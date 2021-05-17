print('=' * 25)
print('  10 TERMOS DE UMA PA')
print('=' * 25)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = (primeiro + (10 -1) * razao) + razao # a razao extra adicionada é para o laço
for c in range(primeiro, decimo, razao):
    print(c, end=' -> ')
print('ACABOU')
