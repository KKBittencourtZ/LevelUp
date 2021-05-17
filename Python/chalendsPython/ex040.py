nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média do aluna é {média}.')
if 10 >= média >= 7:
    print('APROVADO')
elif 7 > média >= 5:
    print('Recuperação')
else:
    print('REPROVADO')