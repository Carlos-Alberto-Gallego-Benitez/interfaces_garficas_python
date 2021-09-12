


from tkinter import *  #importamos la libreria de tkinter para crear interfaces

root = Tk() #creamos la interfaz

root.title("Carlos Python") #nos permite darle un titulo a la interfaz

def Sumar(): #creando metodo sumar

    if(var1.get()==""):
        resultado.set("llene el  campo uno")
    elif(var2.get()==""):
        resultado.set("llene el campo dos")
    else:
      resultado.set(int(var1.get())+ int(var2.get())) #linea para combertir dato de string a numero para operacion


def Restar():#creando metodo restar

    if (var1.get() == ""):
        resultado.set("llene el  campo uno")
    elif (var2.get() == ""):
        resultado.set("llene el campo dos")
    else:
        resultado.set(int(var1.get()) - int(var2.get()))  # linea para combertir dato de string a numero para operacion


var1 = StringVar() #declarando las variables
var2 = StringVar()
resultado = StringVar()

entrada1 = Entry(root) #entrada de texto
entrada1.pack()
entrada1.config(bd=10, font = "Curier,20", justify="center", textvariable = var1) #doy margenes colores y agrego las variables que van recibir el valor


entrada2 = Entry(root) #entrada de texto
entrada2.pack()
entrada2.config(bd=10, font = "Curier,20", justify="center", textvariable = var2) #doy margenes colores y agrego las variables que van recibir el valor

entrada3 = Entry(root) #entrada de texto
entrada3.pack()
entrada3.config(bd=10, font = "Curier,20", justify="center", state="disable", textvariable = resultado) #doy margenes colores y agrego las variables que van recibir el valor




boton = Button(root, text = "Sumar")
boton.pack()
boton.config(bg = "Gray", padx = 18, pady = 10, command = Sumar) #con el command se llama a la funcion que hace la operacion

boton = Button(root, text = "Restar")
boton.pack()
boton.config(bg = "Red", padx = 18, pady = 10, command = Restar)



root.mainloop() # nos permite que la interfaz grafica se mantenga abierta es indispensable utilizar el mainloop