import imapclient, pyzmail, subprocess, text_me, click, sys, logging
from tendo import singleton


me = singleton.SingleInstance()


logging.basicConfig(
    handlers=[logging.FileHandler("email_control.log"), logging.StreamHandler()],
    format="%(asctime)s -  %(levelname)s -  %(message)s",
    datefmt="%d/%m/%Y %I:%M:%S %p",
)
logger = logging.getLogger()


PATH = "C:/Program Files/qBittorrent/qbittorrent.exe"


def search_emails(password: str) -> list[str]:
    imap = imapclient.IMAPClient("imap-mail.outlook.com", ssl=True)

    try:
        imap.login("xxxxxxxxxx@email.com", password)
    except imapclient.exceptions.LoginError:
        logger.exception("Login to IMAP failed")
        sys.exit(1)

    logger.info("Login to IMAP successful")

    imap.select_folder("Inbox", readonly=False)

    UIDs = imap.search(["SUBJECT", "Open sesame", "FROM", "xxxxxxxxxx@email.com"])
    logging.info(f"UIDs: {UIDs}")

    message_contents = []
    for UID in UIDs:
        raw_messages = imap.fetch([UID], ["BODY[]"])

        message = pyzmail.PyzMessage.factory(raw_messages[UID][b"BODY[]"])
        plaintext_part_of_message = message.text_part.get_payload().decode(
            message.text_part.charset
        )

        message_contents.append(plaintext_part_of_message.strip())

        # imap.delete_messages(UID)

        # imap.expunge() "Some email providers automatically expunge emails deleted with delete_messages(). if not, uncomment this line"

    imap.logout()
    logger.info("logout of IMAP successful")

    return message_contents


def check_for_info_hash(message_contents: list[str]) -> list[str]:
    return [content for content in message_contents if len(content) == 40]


@click.command()
@click.option(
    "--logLevel",
    "-l",
    default=logging.INFO,
    type=int,
    help="set the logging level",
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
    A utility to search emails for an info hash and automatically donload the torrent
    """
    logger.setLevel(loglevel)

    message_contents = search_emails(password)

    if not message_contents:
        logger.info("Command email was empty")
        sys.exit(0)

    logger.info(f"message_contents: {message_contents}")

    info_hashes = check_for_info_hash(message_contents)
    logger.info(f"info_hashes: {info_hashes}")

    if not info_hashes:
        logger.info("No command emails found")
        sys.exit(0)

    for info_hash in info_hashes:
        qBitTorrent = subprocess.Popen([PATH, info_hash], shell=False)
        # text_me.text_myself("Downloading...")
        logger.info("Downloading...")

        if qBitTorrent.wait() == 0:
            # text_me.text_myself("Download complete")
            logger.info("Download complete")


main()
