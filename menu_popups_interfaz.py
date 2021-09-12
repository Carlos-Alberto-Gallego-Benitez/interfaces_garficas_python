from tkinter import*
from tkinter import messagebox #libreria de alertas

def Salir(): #metodo para crear la alerta de confirmacion

    i = messagebox.askquestion("Salir","¿Estas seguro de salir?")#mensaje para la alerta

    if(i == "yes"): #validamos que la confirmacion sea verdadera
        root.destroy() #destruimos la interfaz grafica

def Acerca():#metdo para la mstrar mensaje de ayuda

    messagebox.showinfo("Information","Te ayudaremos Wee.")#mensaje de alerta

def licencia():

    messagebox.showwarning("Alert", "Alerta licencia fallando")

def Error():
    messagebox.showerror("Fataling","Hubo un error en la nasa vamos a explotar")

def Nose(): #metodo para crear la alerta de confirmacion

    messagebox.askquestion("Salir","¿Estas seguro que no sabes?")#mensaje para la alerta

root = Tk()


barraMenu = Menu(root)#CREAMOS EL MENU DENTRO DE LA INTERFAZ ROOT
root.config(menu = barraMenu)#metemos el menu dentro de la interfaz
ArchivoMenu = Menu(barraMenu, tearoff = 0)#lo que va a contener el menu

barraMenu.add_cascade(label = "Archivo", menu = ArchivoMenu)#atrivutos para el menu
ArchivoMenu.add_command(label = "Archivo 1") #creamos las opciones
ArchivoMenu.add_separator()#para separar las opciones
ArchivoMenu.add_command(label = "Archivo 1")
ArchivoMenu.add_separator()#para separar las opciones
ArchivoMenu.add_command(label = "Archivo 1")


ArchivoEditar = Menu(barraMenu, tearoff = 0)#creamos la otra opcion le decimos donde va a estar
barraMenu.add_cascade(label = "Ejemplo2", menu = ArchivoEditar)#le agregamos un nombre
ArchivoEditar.add_command(label = "Ejemplo 3")# y le agregamos las opciones
ArchivoEditar.add_separator()#agregamos los espacios
ArchivoEditar.add_command(label = "Ejemplo 4")
ArchivoEditar.add_separator()
ArchivoEditar.add_command(label = "Ejemplo 5")

ArchivoAyuda = Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label = "Ayuda", menu = ArchivoAyuda)
ArchivoAyuda.add_command(label = "Ayudaaaaaa", command =  Acerca)
ArchivoAyuda.add_separator()
ArchivoAyuda.add_command(label = "Salir", command = Salir) # en esta linea le decimos para que haga accion a el metodo de salir
ArchivoAyuda.add_separator()
ArchivoAyuda.add_command(label = "Liceencia", command = licencia)
ArchivoAyuda.add_separator()
ArchivoAyuda.add_command(label = "Error", command = Error)
ArchivoAyuda.add_separator()
ArchivoAyuda.add_command(label = "No se", command = Nose)
root.mainloop()