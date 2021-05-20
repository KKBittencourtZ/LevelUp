from datetime import date
cadastro = dict()
while True:
    cadastro['Nome'] = str(input('Nome: '))
    cadastro['Idade'] = date.today().year - int(input('Ano de nascimento: '))
    cadastro['CTPS'] = int(input('Carteira de trabalho (0 se não tem): '))
    if cadastro['CTPS'] == 0:
        break
    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = float(input('Salário: R$ '))
    cadastro['Aposentadoria'] = cadastro['Contratação'] + 35 - (date.today().year - cadastro['Idade'])
    break
print('~ ' * 20)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
