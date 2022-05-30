from PySimpleGUI import PySimpleGUI as sg
from time import sleep



# texto_modificado = []
# Layout
sg.theme('Reddit')
Layout = [
    [sg.Input(key='Texto' ,size=(100, 20))],
    [sg.Button('Iniciar',pad=(300, 1))],
    [sg.Output(size=(100, 20))]
]

# texto_modificado = texto

# Janela
janela = sg.Window('Dynamic 001', Layout)


# Funcionalidades
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == 'Iniciar':
        sleep(0.1)
        print(valores['Texto'])
        valores['Texto'] = ''
        


