import PyPDF2


pdf = open("meetingminutes.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf)
pdf_writer = PyPDF2.PdfFileWriter()

for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    pdf_writer.addPage(page)

pdf_writer.encrypt("ambition")
output_pdf = open("meetingminutes_encrypted.pdf", "wb")
pdf_writer.write(output_pdf)
output_pdf.close()
pdf.close()
