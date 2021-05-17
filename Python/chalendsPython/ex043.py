massa = float(input('Qual é seu peso: Kg'))
altura = float(input('Qual é a sua altura: M'))
imc = massa / (altura * altura)
print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif imc <= 25:
    print('Você está PESO IDEAL')
elif imc <= 30:
    print('Você está SOBREPESO')
elif imc <= 40:
    print('Você está OBESIDADE')
else:
    print('Você está OBESIDADE MÓRBIDA!')
