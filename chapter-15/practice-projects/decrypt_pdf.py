import PyPDF2, os, click


INPUT_DIR = "decrypt-pdf-encrypted"
OUTPUT_DIR = "decrypt-pdf"


def decrypt_pdf(password: str) -> None:  # password is swordfish.
    for foldername, _, filenames in os.walk(INPUT_DIR):
        for filename in filenames:
            pdf = open(f"{foldername}/{filename}", "rb")
            pdf_reader = PyPDF2.PdfFileReader(pdf)

            # If password is incorrect .decrypt() returns 0, if file has no password .decrypt() returns KeyError.
            try:
                if pdf_reader.decrypt(password) == 0:
                    print(f"Password for {filename} is incorrect")
                    continue
            except KeyError as _:  ##### just except KeyError: if not printing error?
                print(f"{filename} is not encrypted")

            pdf_writer = PyPDF2.PdfFileWriter()

            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page)

            output_pdf = open(f"{OUTPUT_DIR}/{filename[:-4]}_decrypted.pdf", "wb")
            pdf_writer.write(output_pdf)
            output_pdf.close()
            pdf.close()


@click.command()
@click.option(
    "--password",
    "-p",
    prompt=True,
    hide_input=True,
    type=str,
    required=True,
    help="your password (used to decrypt pdf's)",
)
def main(password: str) -> None:
    """
    A utility to decrypt PDF files with a password.
    """
    decrypt_pdf(password)


main()
