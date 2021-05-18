print('-' * 30)
print('     LOJA SUPER BARATÃO')
print('-' * 30)
total = contmaior = menor = 0
continua = produtomenor = ''
while continua is not 'N':
    item = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$'))
    total += preço
    if preço > 1000:
        contmaior += 1
    if total == preço:
        menor = preço
        produtomenor = item
    elif preço < menor:
        menor = preço
        produtomenor = item
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'NS':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('-------- FIM DO PROGRAMA --------')
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {contmaior} produto(s) custando mais de R$1.000,00.')
print(f'O produto mais barato foi {produtomenor} que custa R${menor:.2f}.')
