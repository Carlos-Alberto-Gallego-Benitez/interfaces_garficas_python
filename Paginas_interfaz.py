import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("400x300")
root.title("Paginas")

cuadromadre = ttk.Notebook(root) #ccreamos la nota o contenedor
cuadromadre.pack(pady =10, expand = "True") #le damos la margen del ancho de la interfaz

frame1 = ttk.Frame(cuadromadre, width=400, height=280)#creamos los frame a la interfaz dentro de la nota
frame2 = ttk.Frame(cuadromadre, width=400, height=280)#

cuadromadre.add(frame1, text="Cuadro 1")#agregamos los frame ala nota
cuadromadre.add(frame2, text="Cuadro 2")

lebol = ttk.Label(frame1, text="Estas de dentro del cuadro1")# le damos un vaor al frame
lebol.pack(expand="True")






root.mainloop()