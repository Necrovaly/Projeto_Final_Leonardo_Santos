import pyautogui
import time 


time.sleep(5) #Coloquei um Delay de 5 segundos para dar tempo de colocar o ponteiro do mouse no lugar desejado
print(pyautogui.position())  #Aqui é pra achar a posição do mouse
pyautogui.press("Home")

