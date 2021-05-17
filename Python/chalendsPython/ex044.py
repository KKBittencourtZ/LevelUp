print('=' * 10, 'LOJA', '=' * 10)
compra = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    valor = compra - (compra * 0.1)
elif opção == 2:
    valor = compra - (compra * 0.05)
elif opção == 3:
    valor = compra
    vezes = compra / 2
    print(f'Sua compra será parcelada em {vezes}x de R${valor:.2f} SEM JUROS')
elif opção == 4:
    vezes = int(input('Quantas parcelas? '))
    valor = compra + (compra * 0.2)
    print(f'Sua compra será parcelada em {vezes}x de R${valor / vezes} COM JUROS.')
else:
    valor = compra
    print(f'Opção inválida, tente novamente!')
print(f'Sua compra de R${compra:.2f} vai custar R${valor:.2f} no final.')
