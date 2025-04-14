import pyautogui

email = pyautogui.prompt(text="Digite o seu email",title="informaçoes obrigatorias") 
print(email) 
senha = pyautogui.prompt(text="digite a sua senha",title="infomaçoes obrigatorias")
print(senha)
pyautogui.moveTo(306,945 ,duration=3)
pyautogui.doubleClick()
pyautogui.hotkey("ctrl","c")
pyautogui.moveTo(1386,142,duration=2)
pyautogui.click()
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
pyautogui.moveTo(306,962 ,duration=3)
pyautogui.doubleClick()
pyautogui.hotkey("ctrl","c")
pyautogui.moveTo(1350,160,duration=2)
pyautogui.click()
pyautogui.hotkey("ctrl","v")

#maneira corrigida de fazer 
...
import pyautogui

email= pyautogui.prompt(text="digite seu email",title="dados de login")
senha= pyautogui.password(text="digite sua senha",title="dados de login",mask="*")
#MASk serve para deixar a senha "invisivel"
pyautogui.click(1660,300,duration=2)
pyautogui.typewrite(email)
pyautogui.press("enter")
pyautogui.typewrite(senha)
...