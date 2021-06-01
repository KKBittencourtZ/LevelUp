import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

leitor_df = pd.read_excel(r"C:\Users\CésarAugusto\Documents\ProjectGitHub\LevelUp\Python\Testcomxl\bbtk.xlsx", engine='openpyxl')
print(leitor_df)


# O código abaixo é usado para fazer gráfico em barra da planilha
leitor_df.plot(kind='bar')
plt.show()
