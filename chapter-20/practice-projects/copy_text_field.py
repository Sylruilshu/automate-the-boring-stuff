import pyautogui, logging, pyperclip, click, sys


logging.basicConfig(
    handlers=[logging.FileHandler("copy_text_field.log"), logging.StreamHandler()],
    format="%(asctime)s -  %(levelname)s -  %(message)s",
    datefmt="%d/%m/%Y %I:%M:%S %p",
)
logger = logging.getLogger()


def copy_text_field(title: str) -> None:

    windows = pyautogui.getWindowsWithTitle(title)

    if windows:
        window = windows[0]
    else:
        logger.error(f"No window matching '{title}' was found")
        sys.exit(1)

    window.activate()
    window.restore()
    logger.info(f"{title} window is active")

    pyautogui.click(window.left + 150, window.top + 150)

    pyautogui.hotkey("ctrl", "a")
    logger.info("Contents selected")
    pyautogui.hotkey("ctrl", "c")
    logger.info("Copied contents to clipboard")

    print(pyperclip.paste())
    logger.info("Pasted contents from clipboard")

    window.minimize()


@click.command()
@click.option(
    "--loglevel",
    "-l",
    default=logging.INFO,
    type=int,
    help="set the logging level",
)
@click.option(
    "--title",
    "-t",
    default="nope.avi",
    type=str,
    help="title of the application (located in the bar, at the top of the window)",
)
def main(loglevel: int, title: str) -> None:
    """
    A utility to automate copying and pasting contents from a notepad document
    """
    logger.setLevel(loglevel)

    copy_text_field(title)


main()
