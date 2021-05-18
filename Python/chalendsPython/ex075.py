x = (int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite o último número: ')))
print(f'Você digitou os valores {x}')
print(f'O valor 9 apareceu {x.count(9)} vezes')
if 3 in x:
    print(f'O valor 3 apareceu na {x.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado!')
li = []
print('Os valores pares digitados foram ', end='')
for n in x:
    if n % 2 == 0:
        print(n, end=' ')
        li.append(n)
if len(li) == 0:
    print('nenhum.')
print()
