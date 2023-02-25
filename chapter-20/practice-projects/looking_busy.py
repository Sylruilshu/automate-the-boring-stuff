import pyautogui


try:
    while True:
        pyautogui.move(10, 0)
        pyautogui.move(-10, 0)
        pyautogui.sleep(10)

except KeyboardInterrupt:
    print("Program terminated")
