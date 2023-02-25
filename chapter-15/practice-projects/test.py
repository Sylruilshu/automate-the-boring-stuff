import PyPDF2
from PyPDF2 import utils


# OUTPUT_DIR = "pdf-paranoia-encrypted"
# filename = "meetingminutes.pdf"

# pdf = open(filename, "rb")
# pdf_reader = PyPDF2.PdfFileReader(pdf)
# pdf_writer = PyPDF2.PdfFileWriter()

# for page_num in range(pdf_reader.numPages):
#     page = pdf_reader.getPage(page_num)
#     pdf_writer.addPage(page)

# pdf_writer.encrypt("swordfish1")
# output_pdf = open(f"{OUTPUT_DIR}/{filename[:-4]}_swordfish1.pdf", "wb")
# pdf_writer.write(output_pdf)
# output_pdf.close()
# pdf.close()


pdf = open("meetingminutes_swordfish1.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf)

pdf_writer = PyPDF2.PdfFileWriter()

try:
    check = pdf_reader.decrypt("swordfish")
    if check == 0:
        print("file not decrypted")
except Exception as e:
    print(e)


for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)

output_pdf = open("meetingminutes_decrypted.pdf", "wb")
pdf_writer.write("output.pdf")
output_pdf.close()
pdf.close()


x = 5

if x > 10:
    print(x)
if x > 12:
    print(x + 1)
else:
    print("x is not a numbner")
