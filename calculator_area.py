import tkinter as tk
from tkinter import ttk, messagebox
import math

# Función para calcular el área del cuadrado
def cal_square():
    try:
        lado = float(sideEntry.get())
        area = pow(lado, 2)
        messagebox.showinfo('Área', f'El área del cuadrado es: {area}')
    except ValueError:
        messagebox.showerror('Error', 'Por favor, ingrese un número válido.')

# Función para calcular el área del rectángulo
def cal_rect():
    try:
        base = float(baseEntry.get())
        altura = float(alturaEntry.get())
        area = base * altura
        messagebox.showinfo('Área', f'El área del rectángulo es: {area}')
    except ValueError:
        messagebox.showerror('Error', 'Por favor, ingrese números válidos.')

# Función para calcular el área de un polígono regular
def cal_pol():
    try:
        n = int(sidesEntry.get())
        s = float(lengthEntry.get())
        if n < 3:
            messagebox.showerror('Error', 'Un polígono debe tener al menos 3 lados.')
            return
        area = (n * pow(s, 2)) / (4 * math.tan(math.pi / n))
        messagebox.showinfo('Área', f'El área del polígono es: {area}')
    except ValueError:
        messagebox.showerror('Error', 'Por favor, ingrese números válidos.')

# Declaración de la ventana principal
main = tk.Tk()
main.title('Calculadora de áreas')

# Creación del Notebook para las pestañas
notebook = ttk.Notebook(main)
notebook.pack(pady=20, expand=True)

# Creación de los frames para cada pestaña
frame_square = ttk.Frame(notebook)
frame_rectangle = ttk.Frame(notebook)
frame_polygon = ttk.Frame(notebook)

# Agregar los tabs (pestañas) al Notebook
notebook.add(frame_square, text="Cuadrado")
notebook.add(frame_rectangle, text="Rectángulo")
notebook.add(frame_polygon, text="Polígono")

# Botones y formularios para la tab del cuadrado
sideLabel = tk.Label(frame_square, text='Ingrese el valor de uno de los lados:')
sideLabel.grid(column=0, row=0, pady=10)
sideEntry = tk.Entry(frame_square)
sideEntry.grid(column=1, row=0)
btnCalcSquare = tk.Button(frame_square, text='Calcular', command=cal_square)
btnCalcSquare.grid(column=0, row=1, pady=10)

# Botones y formularios para la tab del rectángulo
base_label = tk.Label(frame_rectangle, text='Ingrese el valor de base:')
base_label.grid(column=0, row=0, pady=10)
baseEntry = tk.Entry(frame_rectangle)
baseEntry.grid(column=1, row=0)
altura_label = tk.Label(frame_rectangle, text='Ingrese el valor de altura:')
altura_label.grid(column=0, row=1, pady=10)
alturaEntry = tk.Entry(frame_rectangle)
alturaEntry.grid(column=1, row=1)
btnCalcRect = tk.Button(frame_rectangle, text='Calcular', command=cal_rect)
btnCalcRect.grid(column=0, row=2, pady=10)

# Botones y formularios para la tab del polígono
sidesLabel = tk.Label(frame_polygon, text='Ingrese el número de lados:')
sidesLabel.grid(column=0, row=0, pady=10)
sidesEntry = tk.Entry(frame_polygon)
sidesEntry.grid(column=1, row=0)
lengthLabel = tk.Label(frame_polygon, text='Ingrese la longitud de un lado:')
lengthLabel.grid(column=0, row=1, pady=10)
lengthEntry = tk.Entry(frame_polygon)
lengthEntry.grid(column=1, row=1)
btnCalcPol = tk.Button(frame_polygon, text='Calcular', command=cal_pol)
btnCalcPol.grid(column=0, row=2, pady=10)

# Ejecución de la aplicación
main.mainloop()
