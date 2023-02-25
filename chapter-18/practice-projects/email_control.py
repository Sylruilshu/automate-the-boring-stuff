import imapclient, pyzmail, subprocess, text_me, click, sys, logging
from tendo import singleton

PATH = "C:/Program Files/qBittorrent/qbittorrent.exe"

logging.basicConfig(
    filename="email_control.log",
    level=logging.INFO,
    format="%(asctime)s -  %(levelname)s -  %(message)s",
    datefmt="%d/%m/%Y %I:%M:%S %p",
)

singleton.SingleInstance()


def search_emails(password: str) -> list | None:
    imap = imapclient.IMAPClient("imap-mail.outlook.com", ssl=True)

    try:
        imap.login("xxxxxxxxxx@email.com", password)
    except imapclient.exceptions.LoginError:
        logging.info("")
        logging.error("Login to IMAP failed")
        sys.exit(1)

    logging.info("")
    logging.info("Login to IMAP successful")

    imap.select_folder("Inbox", readonly=False)

    UIDs = imap.search(["SUBJECT", "Open sesame", "FROM", "xxxxxxxxxx@email.com"])
    logging.info(f"UIDs: {UIDs}")

    if UIDs:
        message_contents = []
        for i in range(len(UIDs)):
            raw_messages = imap.fetch([UIDs[i]], ["BODY[]"])

            message = pyzmail.PyzMessage.factory(raw_messages[UIDs[i]][b"BODY[]"])
            plaintext_part_of_message = message.text_part.get_payload().decode(
                message.text_part.charset
            )

            message_contents.append(plaintext_part_of_message.strip())

            # imap.delete_messages(UIDs[i])

            # imap.expunge() "Some email providers automatically expunge emails deleted with delete_messages(). if not, uncomment this line"

        imap.logout()
        logging.info("logout of IMAP successful")
        return message_contents
    else:
        return None


def check_for_info_hash(message_contents: list | None) -> list | None:
    if message_contents:
        message_contents_without_junk = [
            content for content in message_contents if len(content) == 40
        ]
        return message_contents_without_junk
    else:
        return None


@click.command()
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
def main(password: str) -> None:
    """
    A utility to search emails for an info hash and automatically donload the torrent
    """
    message_contents = search_emails(password)
    logging.info(f"message_contents: {message_contents}")
    info_hashes = check_for_info_hash(message_contents)
    logging.info(f"info_hashes: {info_hashes}")

    if info_hashes == None:
        logging.info("No command emails found")
        print("No command emails found")
        sys.exit(0)

    if info_hashes == []:
        logging.info("Command email was empty")
        print("Command email was empty")
        sys.exit(0)

    for info_hash in info_hashes:
        qBitTorrent = subprocess.Popen([PATH, info_hash], shell=False)
        # text_me.text_myself("Downloading...")
        logging.info("Downloading...")
        print("Downloading...")

        if qBitTorrent.wait() == 0:
            # text_me.text_myself("Download complete")
            logging.info("Download complete")
            print("Download complete")


main()


# LIMITATIONS:
#   - Downloads one file at a time (but can queue multiple files)
#   - Only one info hash per email is currently accepted, can't process multiple info hashes in a single email (will delete as length is not 40)
#   - Cant check if 40 char string is a valid info hash => opens qBitTorrent (problem as it will never close)
#   - If duplicate info hash passed to subprocess.Popen at different times qBitTorrent will never close

# NEED TO CHECK:
#   how to pass password to task scheduler? <----- got to work, but in plaintext (not good)
