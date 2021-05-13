from openpyexcel import Workbook
from openpyexcel.writer.excel import save_workbook

wb = Workbook()

planilha = wb.worksheets[0]

planilha['A1'] = "Livro 1"
planilha['B1'] = "Livro 2"
planilha['C1'] = "Livro 3"
planilha['A2'] = "50"
planilha['B2'] = "340"
planilha['C2'] = "500"

planilha.title = "A"
# wb.save("Python\Testcomxl\Biblioteca.xlsx")
print(planilha)
