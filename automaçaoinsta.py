import webbrowser
from time import sleep
import pyautogui


def logout():
  pyautogui.click(1660,383)
  sleep(2)
  pyautogui.click(96,972)
  sleep(2)
  pyautogui.click(145,896)

while True:
    webbrowser.open("https://www.instagram.com/?flo=true")
    pyautogui.click(1225,350,duration=2)
    pyautogui.write("kaique.pereira")
    pyautogui.click(1198,403,duration=2)
    pyautogui.write("1234567")
    pyautogui.click(1311,471,duration=2)
   #clicar em agora nao
    pyautogui.click(1092,652,duration=8)
 #abrir aba de pesquisa
    pyautogui.moveTo(47,332,duration=6)
    pyautogui.click()
#pesuqisar o nome desejado
    pyautogui.typewrite("nike")
#clicar no perfil desejado
    pyautogui.click(283,389,duration=3)
#clicar na ultima publicaçao
    sleep(2)
    pyautogui.click(683,863,duration=2)
    sleep(1)
    # tentar localizar a imagem do coração
    try:
     coracao2 = pyautogui.locateCenterOnScreen("coracao2.png")
    except Exception as e:
     print(f"Erro ao localizar imagem: {e}")
    coracao2 = None


    sleep(2)
    if coracao2 is not None:
     logout()
     sleep(33333333)

    elif coracao2 == None:
     pyautogui.click(912,828,duration=2)    
    sleep(5)
    pyautogui.click(1131,960,duration=2)
    sleep(5)
    pyautogui.typewrite("gostei demais")
    sleep(2)
    pyautogui.click(1452,960,duration=2)
    logout()
    sleep(303333)
