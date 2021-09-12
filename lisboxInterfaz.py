from tkinter import *

root = Tk()
label = Label(root, text = "Productos")
label.pack()
label.config(bg = "Gray")

def Agrega():#funcion que agrega valor al arreglo

    lista.insert(END,entrada.get())

lista = Listbox(root) #creo la lista y le agrego valores
lista.insert(0, "Pollo")
lista.insert(1, "Arroz")
lista.insert(2, "Frutas")
lista.insert(3, "Vegetales")
lista.insert(4, "Verduras")
lista.pack()

lista.delete(0) #elimino elemento de la lista


#linea para agregar elementos manuales

entrada = Entry(root) #creo la entrada
entrada.pack()

#creo el boton

boton = Button(root, text = "Agregar")
boton.pack()
boton.config(bg = "Blue", padx = 20, pady = 10, command = Agrega) #creamos el boton con la funcion de agregar

root.mainloop()