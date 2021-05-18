from datetime import date
atual = date.today().year
novo = 0
velho = 0
for c in range(1, 8):
    x = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if atual - x < 18:
        novo += 1
    else:
        velho += 1
print(f'Ao todo tivemos {velho} pessoas maiores de idade')
print(f'E também tivemos {novo} pessoas menores de idade.')
