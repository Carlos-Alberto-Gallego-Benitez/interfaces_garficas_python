import tkinter as tk
from  tkinter import ttk

root = tk.Tk()
root.geometry("300x120")
root.title("Barra de progreso")

root.grid()

bd = ttk.Progressbar(root, orient = "horizontal", mode="indeterminate", length="280")#creamoss la barra con las caracteristicas dadas
bd.grid(column=0, row=0, columnspan=2, padx=10, pady=20)## le damos la ubicacion


boton_iniciar = ttk.Button(root, text="Iniciar", command = bd.start)#creamos el boton para encender la barra
boton_iniciar.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)#ubicamos el boton

boton_iniciar = ttk.Button(root, text="Detener", command = bd.stop)#creamos el boton para detener la barra
boton_iniciar.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)#ubicamos el boton

boton_iniciar = ttk.Button(root, text="Cancelar", command = bd.destroy)#creamos el boton para destruir la barra
boton_iniciar.grid(column=0, row=2, padx=10, pady=10, columnspan=2 )#ubicamos el boton

root.mainloop()
