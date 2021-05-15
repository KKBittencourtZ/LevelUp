casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
limite = salario * 0.3
print(f'Para pagar uma casa de R${casa:.2f} em 7 anos a prestação será de R${prestacao:.2f}.')
if prestacao <= limite:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
