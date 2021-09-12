from tkinter import *  #importamos la libreria de tkinter para crear interfaces

root = Tk() #creamos la interfaz

root.title("Carlos Python") #nos permite darle un titulo a la interfaz

root.resizable(1,1) #nos permite controlar las margenes de interfaz

root.iconbitmap("dr4.ico") #con esta linea le damos la imagen de icono

root.config(bg="gray") #con esta linea le damos color a toda la interfaz

root.config(cursor = "boat")

#root.geometry("600x350") #con esta linea le damos margenes personalizadas a la interfaz

#utilizareos el frame

MiFrame = Frame() #llamamos al frame
MiFrame.pack(expand=1) #con esta linea enpaquetamos la interfaz Y damos la direccion de ubicacion
MiFrame.config(width = 300, height =400) #con esta linea controlomos las margenes del paquete
MiFrame.config(cursor = "pirate") #con esta linea se le da estilo al cursor en forma de un pirata
MiFrame.config(bg = "red") #con esta linea le damos color solo al paquete de frame
MiFrame.config(bd = "10")#con esta linea le damos el tamaño del vorde solo al paquete frame
MiFrame.config(relief = "ridge")#con esta linea le damos el estilo al borde

"""" con esto creamos etro paquete

MiFrame1 =Frame()
MiFrame1.pack()
MiFrame1.config(width =300, height =400)
MiFrame1.config(bg = "black") #con esta linea le damos color solo al paquete de frame
MiFrame1.config(bd = "10")#con esta linea le damos el tamaño del vorde solo al paquete frame
MiFrame1.config(relief = "ridge")#con esta linea le damos el estilo al borde """





root.mainloop() # nos permite que la interfaz grafica se mantenga abierta es indispensable utilizar el mainloop

