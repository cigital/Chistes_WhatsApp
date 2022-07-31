import pyautogui as pt
import pyperclip as pp
import webbrowser
from time import sleep
import random

numero = 0

def chiste_random():
    chiste_elegido = random.choice(list(open('chistes.txt')))
    pp.copy(chiste_elegido)
    print(f"Esta es el chiste: {chiste_elegido}")
    return chiste_elegido

def numero_random():
    global numero

    d = {"Contacto1": '+xx xxx xxx xxx x', "Contacto2": '+xx xxx xxx xxx x', "Contacto3": '+xx xxx xxx xxx x', "Contacto4": '+xxx xxx x-xx-xx', "Contacto5": '+xx xxx xxx xxx', "Contacto6": '+xx xxx xxx xxx', "Contact7": '+xx xxx xxx xxx'}

    numero = random.choice(list(d.items()))
    print(f"El numero elegido es {numero[1]}, que es de {numero[0]}")

    return numero

numero_random()

for i in range(2):
    webbrowser.open('https://web.whatsapp.com/send?phone='+numero[1], new=0)
    sleep(90)

    chiste_random()
    pt.hotkey("ctrl", "v")
    pt.press('enter')
