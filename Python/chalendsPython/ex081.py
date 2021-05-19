numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort()
print(f'Os valores em ordem decrescente são {numeros[::-1]}')
print(f'O valor 5', end=' ')
if 5 in numeros:
    print('faz parte dessa lista!')
else:
    print('não foi encontrado na lista!')
