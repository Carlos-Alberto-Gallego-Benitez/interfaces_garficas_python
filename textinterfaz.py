from tkinter import *  #importamos la libreria de tkinter para crear interfaces

root = Tk() #creamos la interfaz

texto = Text(root) #creamos en input tipo texto de tamaño grande
texto.pack()
texto.config(width = 40, height = 15, pady=5, padx=67)# le damos margenes

label =Label(root, text = "Hellow World")#creamos el input
label.pack()
label.config(bg = "Gray", font= "Curier, 20")

root.mainloop()