#Automatizacion escritorio
#https://pyautogui.readthedocs.io/en/latest/keyboard.html



#Importar librería
import pyautogui


#Resolucion de pantalla
#print(pyautogui.size())



#posicion actual del cursor
#print(pyautogui.position())
#x,y = pyautogui.position()


#Verificar si el cursor esta en pantalla
#print(pyautogui.onScreen(x,y))

#Esperar/pausas
#sleep(2)

#Mover el mouse (x, y, tiempo)
#pyautogui.moveTo(100, 500,2)

#Mover a una posicion relativa
#pyautogui.moveRel(500,200,2)

#Arrastrar el mouse (Mantener el click y mover)('left', 'middle', 'right'):
#pyautogui.dragTo(200, 300, button = 'left', duration = 2)
#pyautogui.dragRel(200, 300, button = 'left', duration = 2)

#Click Mouse
#pyautogui.click()
#pyautogui.click(100, 20, 2)

#Doble click
#pyautogui.doubleClick()
#pyautogui.click(clicks = 2)

#Scroll
#down 300
#up -3000
#pyautogui.scroll()


#KEYBOARD FUNCTIONS
#pyautogui.write('')

#Mayusculas
#pyautogui.write("shift", "c")

#Atajos de teclado
#pyautogui.hotkey("ctrl","c")

#EJERCICIO
#print(pyautogui.position())

pyautogui.moveTo(185,878,1)

pyautogui.click()

pyautogui.write('Notepad')

#print(pyautogui.position())
pyautogui.moveTo(200,350,1)

pyautogui.doubleClick()

pyautogui.moveRel(100,0, 1)
pyautogui.click()

pyautogui.write("Hola , esto es una prueba de lo que se puede hacer en programacion", interval = 0.05)