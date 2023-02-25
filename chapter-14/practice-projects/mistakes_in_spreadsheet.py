import ezsheets


spreadsheet = ezsheets.Spreadsheet("1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg")
sheet = spreadsheet[0]

rows = sheet.getRows()

for i in range(2, len(rows)):
    if sheet.getRow(i)[0] == "":
        print(f"End of spreadsheet at row {i}")
        break
    if (int(sheet.getRow(i)[0]) * int(sheet.getRow(i)[1])) != int(sheet.getRow(i)[2]):
        print(f"Error in row {i} - {sheet.getRow(i)}")
