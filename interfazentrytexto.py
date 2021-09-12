from tkinter import *  #importamos la libreria de tkinter para crear interfaces

root = Tk() #creamos la interfaz

root.title("Carlos Python") #nos permite darle un titulo a la interfaz

root.resizable(1,1) #nos permite controlar las margenes de interfaz

root.iconbitmap("dr4.ico") #con esta linea le damos la imagen de icono

frame = Frame(root, width=500, height=400) #creamos un frame

frame.pack() #empaquetamos

entrada = Entry(frame) #creamos un input o entrada de texto
entrada.grid(row =  0, column = 1) #ubicacion del label
entrada.config(justify = "center", state="disabled")

entrada1 = Entry(frame) #creamos un input o entrada de texto
entrada1.grid(row =  1, column = 1) #ubicacion de label
entrada1.config(justify = "center", show="*")

label = Label(frame, text = "Nombre", pady = 9); #label de nombre para la primera entrada
label.grid(row =  0, column = 0);

label1 = Label(frame, text ="Apellido");#label de apellido para la segunda entrada
label1.grid(row =  1, column = 0, padx =5, pady=5);






root.mainloop() # nos permite que la interfaz grafica se mantenga abierta es indispensable utilizar el mainloop