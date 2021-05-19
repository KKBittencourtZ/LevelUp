nome = []
peso = []
while True:
    nome.append(str(input('Nome: ')))
    peso.append(float(input('Peso: ')))
    pergunta = str(input('Quer continuar? [S/N] '))
    if pergunta in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(nome)} pessoas.')
print(f'O maior peso foi de {max(peso):.2f}Kg de ', end='')
cont = peso.count(max(peso))
for x, m in enumerate(peso):
    if m == max(peso):
        print(nome[x], end='')
        cont -= 1
        if cont == 0:
            print('.')
        elif cont == 1:
            print(' e ',end='')
        else:
            print(', ', end='')
print(f'O menor peso foi de {min(peso):.2f}Kg de ',end='')
cont = peso.count(min(peso))
for x, m in enumerate(peso):
    if m == min(peso):
        print(nome[x], end='')
        cont -= 1
        if cont == 0:
            print('.')
        elif cont == 1:
            print(' e ',end='')
        else:
            print(', ', end='')
