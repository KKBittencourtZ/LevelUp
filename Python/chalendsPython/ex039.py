from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
if atual - ano < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento.')
    print(f'Seu alistamento será em {ano + 18}.')
elif atual - ano > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {ano + 18}')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
