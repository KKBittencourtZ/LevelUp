carro = float(input('Qual é a velocidade atual do carro? '))
if carro > 80:
    print('MULTADO! Você excedeu o limite de velocidade permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de RS{(carro - 80) * 7:.2f}!')

print('Tenha um bom dia! Dirija com segurança!')
