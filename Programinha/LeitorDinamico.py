import os


mugiwaras = ['Ruffy', 'Zoro', 'Nami', 'Usoop', 'Sanji', 'Chopper', 'Nico Robin', 'Franky', 'Brook', 'Jinbe']

with open('Programinha\MugiTeam.txt', 'w', newline='') as file:
    for line in mugiwaras:
        file.write(line + os.linesep)
