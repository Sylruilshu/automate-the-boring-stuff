import imapclient, imaplib, pyzmail, bs4, logging, sys, click, re, webbrowser


logging.basicConfig(
    handlers=[logging.FileHandler("email_control.log"), logging.StreamHandler()],
    format="%(asctime)s -  %(levelname)s -  %(message)s",
    datefmt="%d/%m/%Y %I:%M:%S %p",
)
logger = logging.getLogger()

regex = re.compile("unsubscribe", re.I)

imaplib._MAXLINE = 10000000


def search_emails(password: str) -> None:
    imap = imapclient.IMAPClient("imap-mail.outlook.com", ssl=True)

    try:
        imap.login("xxxxxxxxxx@email.com", password)
    except imapclient.exceptions.LoginError:
        logging.error("Login to IMAP failed")
        sys.exit(1)

    logging.info("Login to IMAP successful")

    imap.select_folder("Inbox", readonly=True)

    UIDs = imap.search(["BODY", "unsubscribe"])
    logging.info(f"UIDs: {UIDs}")

    for UID in UIDs:
        raw_messages = imap.fetch([UID], ["BODY[]"])

        message = pyzmail.PyzMessage.factory(raw_messages[UID][b"BODY[]"])
        html_part_of_message = message.html_part.get_payload().decode(
            message.html_part.charset
        )

        soup = bs4.BeautifulSoup(html_part_of_message, "lxml")
        link_element = soup.find("a", text=regex)

        if link_element:
            unsubscribe_link = link_element.get("href")
            webbrowser.open(unsubscribe_link)
            logging.info(f"Opened: {unsubscribe_link}")

    imap.logout()
    logging.info("logout of IMAP successful")


@click.command()
@click.option(
    "--loglevel",
    "-l",
    default=logging.INFO,
    type=int,
)
@click.option(
    "--password",
    "-p",
    prompt=True,
    hide_input=True,
    confirmation_prompt=False,
    type=str,
    required=True,
    help="your password (used to login to outlook.com)",
)
def main(password: str, loglevel: int) -> None:
    """
    A utility to search emails for unsubscribe links and open the webpages
    """
    logger.setLevel(loglevel)

    search_emails(password)


main()
