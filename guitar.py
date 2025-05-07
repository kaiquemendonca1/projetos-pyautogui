import pyautogui
import keyboard
import webbrowser
from time import sleep
webbrowser.open ("https://guitarflash.com")
pyautogui.moveTo(770,704,duration=5)

pyautogui.click(duration=2)
sleep(1)
pyautogui.scroll(-300)
sleep(5)

pyautogui.moveTo(928,528,duration=3)
pyautogui.press("tab")

while keyboard.is_pressed("1") == False:

    if pyautogui.pixelMatchesColor(725,910,(0,150,0)):
        pyautogui.press("a")
        sleep(0.05)

    if pyautogui.pixelMatchesColor(838,910,(255,10,10)):
        pyautogui.press("s")
        sleep(0.05)

    if pyautogui.pixelMatchesColor(949,909,(244,244,2)):
        pyautogui.press("j")
        sleep(0.05)