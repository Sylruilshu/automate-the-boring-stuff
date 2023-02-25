import ezsheets


spreadsheet = ezsheets.Spreadsheet("1P_J_W_imiWcsbzWgNjXCV5GDm0VumZiYLq3emK1Abxo")
sheet = spreadsheet["Responses"]

emails = sheet.getColumn(3)

email_addresses = []

for email in emails[1:]:
    if email == "":
        continue
    email_addresses.append(email)

print(email_addresses)
