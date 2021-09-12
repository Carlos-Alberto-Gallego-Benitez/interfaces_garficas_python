from tkinter import *  #importamos la libreria de tkinter para crear interfaces

root = Tk() #creamos la interfaz

root.title("Carlos Python") #nos permite darle un titulo a la interfaz

root.resizable(1,1) #nos permite controlar las margenes de interfaz

root.iconbitmap("dr4.ico") #con esta linea le damos la imagen de icono

root.config(height =400, width =500)#con esta linea damos margenes

nuevolable = StringVar() #con estas dos lienas enviamos valores al label dinamicamente
nuevolable.set("Melooooo")

label = Label(root, text = "Hellow World")#con esta linea creamos la etiqueta label
label.place(x=200, y=60)#con esta linea le damos margenes
label.config(bg = "blue", fg = "black", font=("Curier",20), textvariable = nuevolable)#con esta linea le damos color al lavel y le damos valores dinamicamente al label


root.mainloop() # nos permite que la interfaz grafica se mantenga abierta es indispensable utilizar el mainloop