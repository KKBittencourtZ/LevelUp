def helpier():
    while True:
        título = 'SISTEMA DE AJUDA PyHELP'
        print('~' * (len(título) + 4))
        print(f'  {título}')
        print('~' * (len(título) + 4))
        ask = str(input('Função ou Biblioteca > ')).lower()
        cabeçalio = f"Acessando o manual do comando '{ask}'"
        print('~' * (len(cabeçalio) + 4))
        print(f'  {cabeçalio}')
        print('~' * (len(cabeçalio) + 4))
        if ask == 'fim':
            print('~' * (len(ask) + 4))
            print('  FIM')
            print('~' * (len(ask) + 4))
            break
        help(ask)
        


#Programa principal
helpier()
