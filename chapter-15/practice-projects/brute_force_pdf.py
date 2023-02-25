import PyPDF2, sys


file = open("dictionary.txt", "r")
words = file.readlines()
file.close()

pdf = open("meetingminutes_encrypted.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf)

for word in words:
    word = word.strip("\n")

    if pdf_reader.decrypt(word) == 0:
        print("...")
        if pdf_reader.decrypt(word.lower()) == 0:
            print("***")
            continue
        else:
            print(f"Password is: {word.lower()}")
            pdf.close()
            sys.exit(0)
    else:
        print(f"Password is: {word}")
        pdf.close()
        sys.exit(0)
