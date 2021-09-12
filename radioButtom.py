from tkinter import *

def Muestra(): #funcion que valida el radiobutton

    if(opcion.get()==1):
        label2.config(text = "eres hombre")
    elif(opcion.get()==2):
        label2.config(text = "eres mujer")

root = Tk()
opcion = IntVar()
var2 = IntVar()

label = Label(root, text = "Elige un opción")
label.pack()
label.config(bg = "Gray")

Radiobutton(root, text="Hombre", variable = opcion, value="1",command = Muestra).pack() #con esta linea creamos el radio boton

Radiobutton(root, text="Mujer", variable = opcion, value="2",command = Muestra).pack() # lo que dije arriba x2

boton = Button(root, text = "verificar")
boton.pack()
boton.config(bg = "Blue", padx=6, pady=5, command = Muestra)

label2 = Label(root)
label2.pack()

root.mainloop()