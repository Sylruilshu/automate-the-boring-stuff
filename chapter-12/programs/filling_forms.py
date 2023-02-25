from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://login.metafilter.com")

userElem = browser.find_element_by_id("user_name")
userElem.send_keys("your_real_username_here")

passwordElem = browser.find_element_by_id("user_pass")
passwordElem.send_keys("your_real_password_here")
