from tkinter import *

root = Tk() #creamos la interfaz
root.title("CheckButton") # le damos un nombre
def Orden():
    lista = ""

    if(color.get()):
        lista += "Dr amarillo \n"
    else:
        lista += "Dr sin color \n"

    if(cilindraje.get()):
        lista += "Dr de cilindraje alto "

    else:
        lista += "DR sin cilindraje"

    mensaje.config(text=lista)
color = IntVar()
cilindraje = IntVar()


frame = Frame(root)#creamos nuestro frame o contenedor
frame.pack()
frame.config(bg = "goldenrod3")

Label(frame,text = "¿Como quieres tu DR 650?", bg = "red").pack(anchor="w") #creamos un label para el titulo
Checkbutton(frame, text = "amarrilla", variable = color, onvalue=1, offvalue = 0, command = Orden).pack(anchor="w")#creamos el chechkbutton

Checkbutton(frame, text = "Alto cilindraje", variable = cilindraje, onvalue=1, offvalue = 0, command = Orden).pack(anchor="w")#creamos el segundo checkbutton

mensaje = Label(frame, bg = "blue") #creamos un label para mostrar las respuesta
mensaje.pack()
mensaje.config(font = "Curier 10")

root.mainloop() #cerramos la interfaz