import ezsheets


spreadsheet = ezsheets.upload("text_to_spreadsheet.xlsx")

spreadsheet.downloadAsExcel("text_to_spreadsheet_downloaded.xlsx")
spreadsheet.downloadAsCSV("text_to_spreadsheet_downloaded.csv")
spreadsheet.downloadAsODS("text_to_spreadsheet_downloaded.ods")
spreadsheet.downloadAsTSV("text_to_spreadsheet_downloaded.tsv")
