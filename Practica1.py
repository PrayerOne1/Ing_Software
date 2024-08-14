import tkinter as tk
from tkinter import ttk, messagebox, ttk

root = tk.Tk()
root.config(width=300, height=400)
root.title("Practica 1")
ttk.Label(root, text="Ingrese nombre").place(x=10, y=20)
tkNombre= tk.Entry(root, width=15)
tkNombre.place(x=10, y=50)

def mostrar_Nombre():
    nombre= tkNombre.get()
    messagebox.showinfo(message="Hola "+nombre, title="Resultado")

btnShow = tk.Button(root, text= "Mostrar", command=mostrar_Nombre)
btnShow.place(x=10, y=80)

root.mainloop()
