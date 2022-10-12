import pyautogui as py
import time

print("Bot iniciado")
while True:
    bolhas = py.locateOnScreen('bolhas.png', confidence= 0.75)
    if bolhas != None:
        vara = py.locateOnScreen('vara.png', confidence=0.75)
        vara_x, vara_y = py.center(vara)
        py.moveTo(vara_x, vara_y, 1)
        py.click()
        time.sleep(1)
        py.click()

        bolhas_x, bolhas_y = py.center(bolhas)
        py.moveTo(bolhas_x, bolhas_y, duration= 0.5)
        py.click()


