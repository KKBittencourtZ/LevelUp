dias_alugado = int(input('Quantos dias alugados? '))
km_rodado = float(input('Quantos Km rodados? '))
valor_diario = dias_alugado * 60
valor_Km = km_rodado * 0.15
total_a_pagar = valor_diario + valor_Km
print(f'O total a pagar é de R${total_a_pagar:.2f}')
