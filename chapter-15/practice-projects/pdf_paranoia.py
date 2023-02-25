import PyPDF2, os, click, shutil


INPUT_DIR = "pdf-paranoia"
OUTPUT_DIR = "pdf-paranoia-encrypted"


def encrypt_pdf(password: str) -> None:  # password is swordfish.
    for foldername, _, filenames in os.walk(INPUT_DIR):
        for filename in filenames:
            pdf = open(f"{foldername}/{filename}", "rb")
            pdf_reader = PyPDF2.PdfFileReader(pdf)
            pdf_writer = PyPDF2.PdfFileWriter()

            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page)

            pdf_writer.encrypt(password)
            output_pdf = open(f"{OUTPUT_DIR}/{filename[:-4]}_encrypted.pdf", "wb")
            pdf_writer.write(output_pdf)
            output_pdf.close()
            pdf.close()


def check_pdf_is_encrypted(password: str) -> None:
    filenames = os.listdir(OUTPUT_DIR)

    for filename in filenames:
        pdf = open(f"{OUTPUT_DIR}/{filename}", "rb")
        pdf_reader = PyPDF2.PdfFileReader(pdf)

        # If password is incorrect .decrypt() returns 0, if file has no password .decrypt() returns KeyError.
        try:
            if pdf_reader.decrypt(password) == 0:
                print(f"Password for {filename} is incorrect")
        except KeyError as _:
            print(f"{filename} is not encrypted")


@click.command()
@click.option(
    "--password",
    "-p",
    prompt=True,
    hide_input=True,
    type=str,
    required=True,
    help="your password (used to encrypt pdf's)",
)
def main(password: str) -> None:
    """
    A utility to encrypt PDF files with a password.
    """
    encrypt_pdf(password)
    check_pdf_is_encrypted(password)
    # os.remove("pdf-paranoia") # can use but have to delete files individually
    # shutil.rmtree(INPUT_DIR)
    # os.mkdir(INPUT_DIR)


main()
