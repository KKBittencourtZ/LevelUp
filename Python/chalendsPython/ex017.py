from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
# hip = ((co ** 2) + (ca ** 2)) ** 0.5
hip = hypot(co, ca)
print(f'A hipotenusa vai medir {hip:.2f}.')
