from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://inventwithpython.com")
linkElem = browser.find_element_by_link_text("Read Online for Free")
type(linkElem)

linkElem.click()  # follows the "Read Online for Free" link
