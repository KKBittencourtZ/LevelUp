def maior(*x):
    números = []
    números.append(list(x[:]))
    print('=' * 30)
    print('Analisando valores passados...')
    if len(x) > 0:
        for l, p in enumerate(x):
            print(p, end=' ')
        print(f'Foram passados {len(x)} valores ao todo.')
        print(f'O maior valor informado foi {max(x)}')
    else:
        print('Não foi digitado nenhum valor !!!')


maior(2, 9, 4, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
