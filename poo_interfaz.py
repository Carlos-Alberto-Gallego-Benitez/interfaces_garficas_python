import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo #para mostra mensajes de elerta

class App(tk.Tk):
    def __init__(self):#se inicializa el constructor
        super().__init__()#se llama a el super y se incializa el constructor

        #configuracion de la interfaz

        self.title("Vista POO")
        self.geometry("300x50")

        #creacion de labes

        self.label = ttk.Label(self, text = "Hola Tkinter")#se crea una etiqueta label
        self.label.pack()

        self.boton = ttk.Button(self, text = "Haz click")#se crea un boton que va a mostra una alerta de mensaje
        self.boton['command'] = self.boton_accion
        self.boton.pack()

    def boton_accion(self): #para mostrar la alerta cuando se de clic en el boton
        showinfo(title="Information", message="Hellow world")#lo que se va a mostra en la alerta

if __name__ == "__main__":
    app = App()
    app.mainloop()