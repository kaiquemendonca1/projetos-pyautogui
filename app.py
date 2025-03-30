import pyautogui
from time import sleep
pyautogui.moveTo(1376,527,duration=0.5)
for i in range(100):
   sleep(0.1)
   pyautogui.click()