from tkinter import *

I =0
def click(valor): #metodo para agregar los valores a la entrada de texto

    global I
    entrada1.insert(END, valor)#se le agrega el valor a la entrada de texto(input)
    I += 1
def eliminar():#para eliminar valores de la entrad de texto

    entrada1.delete(0) #para decirle de donde hasta donde va a eliminar

def operaciones(): #para hacer la operacion segun el signo escogido por el usuario
    operacion = entrada1.get() #tomamos los valores de entrada de texto
    resultado = eval(operacion)#se los enviamos a la funcion eval la cal es encargada de recibir tres valores segun su estructura eval(código,globals,locals)
    entrada1.delete(0, END)
    entrada1.insert(0, resultado)

root = Tk()
root.title("Mi calculadora")

entrada1 = Entry(root, font="Curier 20")#se crea la priemera entrada de texto para recibir valores
entrada1.grid(row=0, column=0, columnspan=4)#para decirle que ocupe dos columnas

#botones

boton1 = Button(root, text="1", width = 5, height = 2, command=lambda:click(1))#la funcion lambda nos permite pasar los arguemntos ala funcion que deseemosen tan solo una linea
boton2 = Button(root, text="2", width = 5, height = 2, command=lambda:click(2))
boton3 = Button(root, text="3", width = 5, height = 2, command=lambda:click(3))
boton4 = Button(root, text="4", width = 5, height = 2, command=lambda:click(4))
boton5 = Button(root, text="5", width = 5, height = 2, command=lambda:click(5))
boton6 = Button(root, text="6", width = 5, height = 2, command=lambda:click(6))
boton7 = Button(root, text="7", width = 5, height = 2, command=lambda:click(7))
boton8 = Button(root, text="8", width = 5, height = 2, command=lambda:click(8))
boton9 = Button(root, text="9", width = 5, height = 2, command=lambda:click(9))
boton0 = Button(root, text="0", width = 16, height = 2, command=lambda:click(0))

#opciones

boton_borrar = Button(root, text="DEL", width = 5, height = 2, command=eliminar)
boton_parentesis1 = Button(root, text="(", width = 5, height = 2, command=lambda:click("("))
boton_parentesis2 = Button(root, text=")", width = 5, height = 2, command=lambda:click(")"))
boton_punto = Button(root, text=".", width = 5, height = 2, command=lambda:click("."))

#operaciones

boton_div = Button(root, text="/", width = 5, height = 2, command=lambda:click("/"))
boton_sum = Button(root, text="+", width = 5, height = 2, command=lambda:click("+"))
boton_multi = Button(root, text="*", width = 5, height = 2, command=lambda:click("*"))
boton_rest = Button(root, text="-", width = 5, height = 2, command=lambda:click("-"))
boton_igual = Button(root, text="=", width = 5, height = 2, command=operaciones)

#ordenar botones por filas y columnas con grid

boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_multi.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_sum.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_rest.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)



root.mainloop()