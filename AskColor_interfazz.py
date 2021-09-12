import tkinter as tk
from tkinter.colorchooser import askcolor

root = tk.Tk()
root.title("AskColor")
root.geometry("300x150")


def CambiaColor(): #funcion para cambiar color
    color = askcolor(title = "Tkinter colores") #para darle el nombre a la ventana de seleccion de color
    root.config(bg=color[1]) #se aplica el color seleccionado a la interfaz

tk.Button( #se crea el boton
    text ="Cambiar color",#se le da el texto al boton
    command=CambiaColor#para decirle hacia a donde va hacer axion
).pack(expand = True) #empaquetamos

root.mainloop()