from ctypes import sizeof
from typing import Sized
from PySimpleGUI import PySimpleGUI as sg



# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário:', size=(6, 1)), sg.Input(key='usuario', size=(20, 1))],    # O parametro size=(20, 1) foi adicionado posteriormente para dar uma melhor experiência ao usuário.
    [sg.Text('Senha:', size=(6, 1)), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de Login', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'cesar' and valores['senha'] == '123':
            print('Bem-vindo ao Projeto Simples')
