from random import randint
números = (randint(1, 9), randint(1, 9), randint(1, 9),
            randint(1, 9), randint(1, 9))
print('Os números são ', end='')
for n in números:
    print(n, end=' ')
print(f'\nO maior é {max(números)}')
print(f'O menor é {min(números)}')
