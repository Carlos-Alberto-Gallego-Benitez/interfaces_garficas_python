import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def seleccion(opcion): #funcion para agregar valores recibidos de los respectivos botones
    print(opcion)


ttk.Button(root, text = "Python", command=lambda: seleccion("Monty Python")).pack() #botones
ttk.Button(root, text = "Php", command=lambda: seleccion("php")).pack()
ttk.Button(root, text = "Javascript", command=lambda: seleccion("Javascript")).pack()

root.mainloop()