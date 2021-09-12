from tkinter import *
from tkinter import filedialog

root = Tk()

def Abri():#metodo para la interfaz de tipo file que cargara un archivo del ordenador
    archivo = filedialog.askopenfilename(title = "Abrir", initialdir = "D:",filetypes =(("imagenes","*.png"),("imagenes","*.jpng")))#para abrir el explorador de archivo y cargar un archivo tipo file(input tipo file),
    # se le dice initialdir para que sepa desde donde va abrir el explorador de archivos y se le dice filetypes para decrle los farmatos de archivos que va a buscar    print(archivo)#se imprime la ruta del archivo cargado

Button(root, text="Archivos", command=Abri).pack() # se crea un boton el cual llama al metodo de tipo file Abrr

root.mainloop()