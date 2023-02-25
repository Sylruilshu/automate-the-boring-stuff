import pyautogui, sys, logging
from time import sleep


MESSAGES = [
    {
        "name": "Test 1",
        "message": "Hello, world!",
    },
    {
        "name": "Test 2",
        "message": "This is a test",
    },
    {
        "name": "Test 3",
        "message": "The cake is a lie",
    },
]

APPLICATION_TITLE = "Chat — Mozilla Firefox"


logging.basicConfig(
    handlers=[
        logging.FileHandler("instant_messenger_bot.log"),
        logging.StreamHandler(),
    ],
    format="%(asctime)s -  %(levelname)s -  %(message)s",
    datefmt="%d/%m/%Y %I:%M:%S %p",
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


windows = pyautogui.getWindowsWithTitle(APPLICATION_TITLE)

try:
    google_chat_window = windows[0]
except IndexError:
    logger.exception(f"No window found matching: {APPLICATION_TITLE}")
    sys.exit(1)

logger.info(f"'{APPLICATION_TITLE}' window found")

google_chat_window.activate()
google_chat_window.maximize()

sleep(1)

screenshot = pyautogui.screenshot()

if screenshot.getpixel((138, 440)) == (
    32,
    119,
    233,
):  # Initially validate the link is present
    logger.info("Link present")
    for i in range(len(MESSAGES)):
        if pyautogui.pixelMatchesColor(
            138, 440, (32, 119, 233)
        ):  # Validate the link is still present after sending message.
            logger.info("Link still present")
            pyautogui.moveTo(138, 440)
            pyautogui.click()
            logger.info("Link clicked")

            sleep(1)
            pyautogui.write(MESSAGES[i]["name"])
            sleep(1)
            pyautogui.press("enter")
            logger.info(f"Chat with '{MESSAGES[i]['name']}' opened")
            sleep(1)
            pyautogui.write(MESSAGES[i]["message"])
            pyautogui.press("enter")
            logger.info(f"Message sent: {MESSAGES[i]['message']}")
else:
    logger.exception("Link not present")
    sys.exit(1)

sleep(1)

if pyautogui.pixelMatchesColor(
    78, 140, (0, 131, 45)
):  # Validates home button is present
    pyautogui.moveTo(78, 140)
    pyautogui.click()
    logger.info("Home button clicked")
else:
    logger.exception("Home button not found")
    sys.exit(1)
