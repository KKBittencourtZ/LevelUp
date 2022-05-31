import PySimpleGUI as sg
from time import sleep


class LDinamica:
    def __init__(self):
        # Layout
        layout = [
            [sg.Button('Play')],
            [sg.Checkbox('60', key='easy') ,sg.Checkbox('150', key='mid'), sg.Checkbox('240', key='hard')],
            [sg.Input(key='Mensagem', size=(50, 20))],
            [sg.Output(size=(50, 10))]
        ]
        
        # Janela
        self.janela = sg.Window('Leitura Dinâmica').layout(layout)
        
        
        
        
    def Iniciar(self):
        while True:
            # Conversão do texto
            self.button, self.values = self.janela.read()
        
            mensagem = self.values['Mensagem']
            print(mensagem)



programinha = LDinamica()
programinha.Iniciar()
