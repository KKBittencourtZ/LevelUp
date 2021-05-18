from random import randint
cont = 1
pc = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
chute = int(input('Qual é o seu palpite? '))
while chute != pc:
    cont += 1
    if pc > chute:
        print('Mais... Tente mais uma vez!')
    elif pc < chute:
        print('Menos... Tente mais uma vez!')
    chute = int(input('Qual é o seu palpite? '))
print(f'Acertou com {cont} tentativas. Parabéns !!!')
