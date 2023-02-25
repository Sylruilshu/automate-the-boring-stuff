from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import click, re


# Find better way to wait. until element has loaded??


def send_email(
    email_address: str, password: str, recipient_email: str, message: str
) -> None:

    driver = webdriver.Firefox()
    driver.get("https://www.mail.com/")

    sleep(10)

    login_button_element = driver.find_element(By.ID, "login-button")
    login_button_element.click()

    login_email_text_field_element = driver.find_element(By.ID, "login-email")
    login_email_text_field_element.click()
    login_email_text_field_element.send_keys(email_address)

    login_password_text_field_element = driver.find_element(By.ID, "login-password")
    login_password_text_field_element.click()
    login_password_text_field_element.send_keys(password)
    login_password_text_field_element.submit()

    sleep(10)

    email_link_element = driver.find_element(
        By.CSS_SELECTOR, "#actions-menu-primary > a:nth-child(2)"
    )
    email_link_element.click()

    sleep(10)

    mail_iframe_element = driver.find_element(By.ID, "thirdPartyFrame_mail")
    driver.switch_to.frame(mail_iframe_element)

    compose_emial_link_element = driver.find_element(By.ID, "id5")
    compose_emial_link_element.click()

    sleep(15)

    recipient_text_field = driver.find_element(By.CLASS_NAME, "select2-input")
    recipient_text_field.click()
    recipient_text_field.send_keys(recipient_email)

    compose_message_iframe_element = driver.find_element(
        By.CLASS_NAME, "cke_wysiwyg_frame"
    )
    driver.switch_to.frame(compose_message_iframe_element)

    message_body_text_field = driver.find_element(By.ID, "body")
    message_body_text_field.click()
    message_body_text_field.send_keys(message)

    driver.switch_to.parent_frame()
    send_button_element = driver.find_element(By.ID, "compose-send-button")
    send_button_element.click()

    sleep(3)

    driver.quit()


def validate_email(ctx: click.Context, param: click.Parameter, value: str) -> str:
    email_regex = re.compile(
        r"""(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )""",
        re.VERBOSE,
    )

    match_object = email_regex.search(value)

    if match_object:
        return value
    else:
        raise click.BadParameter("Email is invalid")


@click.command()
@click.option(
    "--email-address",
    "-e",
    type=str,
    required=True,
    help="your username (used to login to mail.com)",
    callback=validate_email,
)
@click.option(
    "--password",
    "-p",
    prompt=True,
    hide_input=True,
    confirmation_prompt=True,
    type=str,
    required=True,
    help="your password (used to login to mail.com)",
)
@click.option(
    "--recipient-email",
    "-r",
    type=str,
    required=True,
    help="the recipients email address",
    callback=validate_email,
)
@click.option(
    "--message",
    "-m",
    type=str,
    default="I just lost the game",
    help="the message to be sent",
)
def main(email_address: str, password: str, recipient_email: str, message: str) -> None:
    """
    A utility to send emails via mail.com
    """
    send_email(email_address, password, recipient_email, message)
    click.echo(click.style("Email sent ✔️", fg="green"))


main()
