import pyautogui
import time

while True:
    time.sleep(3)
    pyautogui.typewrite("Spam!")
    pyautogui.press('enter')
