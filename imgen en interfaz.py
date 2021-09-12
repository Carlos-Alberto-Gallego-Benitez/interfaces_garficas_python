from tkinter import *  #importamos la libreria de tkinter para crear interfaces

root = Tk() #creamos la interfaz

root.title("Carlos Python") #nos permite darle un titulo a la interfaz

root.resizable(1,1) #nos permite controlar las margenes de interfaz

root.iconbitmap("dr4.ico") #con esta linea le damos la imagen de icono

imagen = PhotoImage(file = "facelog.png")#con est linea seleccionamos la imagen y la guardamos en una variable

label = Label(root, image = imagen)#con esta linea agregamos la imagen al label

label.pack()# con esta linea empaquetamos


root.mainloop() # nos permite que la interfaz grafica se mantenga abierta es indispensable utilizar el mainloop