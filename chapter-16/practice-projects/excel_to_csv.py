import os, openpyxl, csv


os.makedirs("csv-files", exist_ok=True)

for excel_file in os.listdir(os.path.join("excel-files", ".")):
    if not excel_file.endswith(".xlsx"):
        continue

    workbook = openpyxl.load_workbook(os.path.join("excel-files", excel_file), "r")

    for sheet_name in workbook.sheetnames:
        sheet = workbook[sheet_name]

        output_csv = open(
            os.path.join("csv-files", excel_file[:-5] + "_" + sheet_name + ".csv"),
            "w",
            newline="",
        )
        output_writer = csv.writer(output_csv)

        for row_num in range(1, sheet.max_row + 1):
            rows = []

            for column_num in range(1, sheet.max_column + 1):
                rows.append(sheet.cell(row_num, column_num).value)

            output_writer.writerow(rows)
        output_csv.close()
