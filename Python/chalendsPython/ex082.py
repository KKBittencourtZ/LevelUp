pares = []
impar = []
todos = []
while True:
    x = int(input('Digite um número: '))
    todos.append(x)
    if x % 2 == 0:
        pares.append(x)
    else:
        impar.append(x)
    pergunta = str(input('Quer continuar? [S/N] '))
    if pergunta in 'Nn':
        break
print('-=' * 30)
print(f'A lista completa é {todos}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impar}')

# Resolução do professor
'''
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Ques continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

'''