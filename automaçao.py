import webbrowser
webbrowser.open("https://cursoautomacao.netlify.app")
import pyautogui
#mover ate a pagina
pyautogui.moveTo(1594,289,duration=2)
#chamar a funçao de descer/subir 
pyautogui.scroll(-1000)
pyautogui.scroll(clicks=-1000,x=0,y=800,)
pyautogui.click(1415,560,duration=2)
pyautogui.write("kaique pereira")
pyautogui.click(1349,588,duration=1)
pyautogui.click(1820,246,duration=2)
#subir e descer a pagina 
pyautogui.scroll(+1000)
pyautogui.scroll(clicks=+1000)
pyautogui.scroll(-1800)
pyautogui.scroll(clicks=-1800)
#clicar e baixar arquivos
pyautogui.click(1401,214,duration=2)
pyautogui.click(1426,367,duration=2.5)
#encerrar ao clicar em OK
pyautogui.alert(text="Terminou",button="OK")
