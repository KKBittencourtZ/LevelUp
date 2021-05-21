from typing import Counter


def escreva(msg):
    n = len(msg) + 4
    print('~' * n)
    print(f'  {msg}')
    print('~' * n)


escreva('Gutavo Guanabara')
escreva('Curso em Python no YouTube')
escreva('CeV')
