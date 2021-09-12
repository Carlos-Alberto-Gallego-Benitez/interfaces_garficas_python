from tkinter import*
from tkinter import messagebox

root = Tk()
root.title("Spinbox")

spin = Spinbox(root, values = ("python", "java", "javascript"))
spin.pack()


spin = Spinbox(root, values = ("Django", "Spring", "Vue"))
spin.pack()

root.mainloop()