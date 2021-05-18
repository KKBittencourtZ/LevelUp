valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor cadastrado com sucesso...')
    else:
        print('Valor duplicado! Não foi adicionado !!!')
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
    print('-=' * 20)
print('-=' * 20)
final = sorted(valores)
print(f'Você digitou os valores {final}')
