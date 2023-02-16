#Automatizacion escritorio
#https://pyautogui.readthedocs.io/en/latest/keyboard.html



#Importar librería
import pyautogui
import time
import opencv

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

############################################################

#UBICAR EN LA PANTALLA

#Localizar la imaen en pantalla
res = pyautogui.locateOnScreen("image.png")

#Indicar las coordenadas del centro de la imagen
editbutton = pyautogui.center(res)

#Mover el mouse al centro de la imagen
pyautogui.moveTo(editbutton)


#Localizar el centro de la imagen en pantalla
pyautogui.locateCenterOnScreen("image.png")
print(res)



#Ejercicio Busqueda en YT
###################################################
# 1.- Abrir nueva pestaña en navegador
# 2.- Buscar youtube.com
# 3.- Buscar el canal al cual quieres suscribirte
# 4.- Click en el canal
# 5.- Click en el boton de suscripcion


#Indicar el nombre del canal que queremos buscar
channel_name = prompt("Enter the channel name:")
print(channel_name)


#Abrir nueva pestaña
pyautogui.hotkey('ctrl','t')
time.sleep(1)

#Buscar Youtube
pyautogui.write("https://www.youtube.com/")
pyautogui.hotkey('enter')
time.sleep(1)

#Buscar el caja de busqueda (Search Box)
x,y = pyautogui.locateCenterOnScreen("image.png", confidence = 0.8)
pyautogui.moveTo(search_button,1)
pyautogui.click()
pyautogui.write(channel_name)
pyautogui.hotkey('enter')

#Buscar el logo del canal (logo)
x,y = pyautogui.locateCenterOnScreen("logo.png", confidence = 0.8)
pyautogui.moveTo(x,y,1)
pyautogui.click()

#Buscar el boton de suscripcion
x,y = pyautogui.locateCenterOnScreen("boton_suscripcion.png", confidence = 0.8)
pyautogui.moveTo(x,y, 1)
pyautogui.click()