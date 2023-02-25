import openpyxl
from pathlib import Path


workbook = openpyxl.load_workbook(Path("text_to_speadsheet.xlsx"))
sheet = workbook.active

first_source_data = open(Path("one.txt"), "r")
first_data = first_source_data.readlines()
first_source_data.close()

second_source_data = open(Path("two.txt"), "r")
second_data = second_source_data.readlines()
second_source_data.close()

print(first_data)
print(second_data)

sheet.column_dimensions["A"].width = len(first_data)
sheet.column_dimensions["B"].width = len(second_data)

# Could check which list is longer using if statement to decide amount of for loop iterations???

# if len(first_data) > len(second_data):
#     for x in range(len(first_data)):
#     sheet[f"A{x + 1}"] = first_data[x]
#     sheet[f"B{x + 1}"] = second_data[x]

# if len(first_data) < len(second_data):
#     for x in range(len(second_data)):
#     sheet[f"A{x + 1}"] = first_data[x]
#     sheet[f"B{x + 1}"] = second_data[x]


for x in range(len(first_data)):
    sheet[f"A{x + 1}"] = first_data[x]
    # sheet[f"B{x + 1}"] = second_data[x]

for y in range(len(second_data)):
    sheet[f"B{y + 1}"] = second_data[y]

workbook.save("text_to_speadsheet.xlsx")


# Change column width based on longest item in lists
# Remove added whitespace from cells (remove \n from items in lists)
