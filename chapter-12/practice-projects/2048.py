from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random


driver = webdriver.Firefox()


def check_exists_by_class_name(element_class_name: str) -> bool:
    try:
        driver.find_element(By.CLASS_NAME, element_class_name)
    except NoSuchElementException:
        return False
    return True


element_exists = check_exists_by_class_name("game-over")
print(element_exists)

driver.maximize_window()
driver.get("https://play2048.co/")

body_element = driver.find_element(By.TAG_NAME, "body")

amount_of_moves = 0

while not element_exists:
    random_number = random.randint(0, 3)
    if random_number == 0:
        print("number = 0")
        body_element.send_keys(Keys.LEFT)

    if random_number == 1:
        print("number = 1")
        body_element.send_keys(Keys.DOWN)

    if random_number == 2:
        print("number = 2")
        body_element.send_keys(Keys.RIGHT)

    if random_number == 3:
        print("number = 3")
        body_element.send_keys(Keys.UP)

    amount_of_moves += 1
    element_exists = check_exists_by_class_name("game-over")
    print(element_exists)

score_container_element = driver.find_element(By.CLASS_NAME, "score-container")
score_with_increment = score_container_element.text
print(score_with_increment)
print(len(score_with_increment))

score = score_with_increment.split("\n")[0]
# score = score[0]
print(score)

print("Moves: " + str(amount_of_moves))
# Moves not accurate. includes illegal moves.
print("Score: " + score)

sleep(2)
driver.quit()

# Stop when you get selenium.common.exceptions.NoSuchElementException: Message: Web element reference not seen before:????
