import openpyxl


workbook = openpyxl.load_workbook("text_to_spreadsheet.xlsx")
sheet = workbook.active

column_cells = sheet.columns

for filename, cells in enumerate(column_cells, 1):
    file = open(f"text-to-spreadsheet/{filename}.txt", "w")

    for cell in cells:
        if cell.value == None:
            continue
        file.write(cell.value + "\n")

    file.close()
