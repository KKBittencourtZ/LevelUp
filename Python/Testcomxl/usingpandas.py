import pandas as pd

# tabela = pd.read_excel("C://ProjectGitHub/LevelUp/Python/Testcomxl/Biblioteca.xlsx")
opçao = 'bbtk.xlsx'
opçao2 = pd.read_excel(opçao, sheet_name='A')

print(opçao2)
