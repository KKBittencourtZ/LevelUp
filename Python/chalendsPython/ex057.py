sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dado inválido, informe seu sexo: [M/F] ')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso!')
