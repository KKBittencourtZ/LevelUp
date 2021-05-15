salário = float(input('Qual é o saláriodo funcionário? R$'))
if salário <= 1250:
    aumento = salário + (salário * 0.15)
else:
    aumento = salário + (salário * 0.1)
print(f'Quem ganhava R${salário:.2f} passa a ganhar R${aumento:.2f} agora.')
