from pyautogui import *
from time import sleep
import sys
import webbrowser

path1='C:\\Users\\andyb\\Desktop\\Whatsapp-Spammer-master\\searchbar.png'  #Paste the path of "searchbar.png" image here         
path2='C:\\Users\\andyb\\Desktop\\Whatsapp-Spammer-master\\msgbox.png'    #Paste the path of "msgbox.png" image here


name = input('Nombre de persona o grupo: ')
no = int(input('Número de veces que el mensaje debe ser enviado: '))
msg = input('Mensaje: ')

urL='https://web.whatsapp.com/'
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
controller = webbrowser.get('chrome')




controller.open(urL)
coOr = None
x = 1

while coOr == None:
    sleep(5)
    coOr = locateOnScreen(path1, minSearchTime=2, grayscale=False, confidence=.4)



x1, y1 = center(coOr)

moveTo(x1, y1)
click()
typewrite(name, interval=0.1)
sleep(2)
press('enter')

"""
c = confirm(
    text="El programa seleccionó a la persona o grupo correcto? Nota: una vez que empezó, no se puede cortar hasta que termine la tarea",
    title='Continuar?', buttons=['Sí', 'Cancelar'])


if c == 'Cancelar':
    sys.exit()
"""
"""
coor2 = None
while coor2 == None:
    coor2 = locateOnScreen(path2, minSearchTime=3, grayscale=False, confidence=.4)

x3, y3 = center(coor2)


moveTo(x3, y3)

click()
sleep(2)
"""
sleep(1)
for i in range(no):
    typewrite(msg)
    press('enter')

print('Programa completado')
