import openpyxl
book = openpyxl.load_workbook("C:\\Users\\TAMIL DON\\Deskto\\pythondata.xlsx")
sheet = book.active

cell=sheet.cell(row=2,column=4)
print(cell.value)







