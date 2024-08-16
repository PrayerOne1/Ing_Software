import tkinter as tk

# Crear la ventana de la calculadora
root = tk.Tk()
root.title("Calculadora")

# Variable para almacenar la expresión matemática
expression = ""

# Función para agregar números y operadores a la expresión
def press_button(value):
    global expression
    expression += str(value)
    equation.set(expression)

# Función para evaluar la expresión
def calculate():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Función para limpiar la pantalla
def clear():
    global expression
    expression = ""
    equation.set("")

# Crear la pantalla de la calculadora
equation = tk.StringVar()
screen = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
screen.grid(columnspan=4)

# Crear botones individuales
btn1 = tk.Button(root, text='1', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button(1))
btn2 = tk.Button(root, text='2', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button(2))
btn3 = tk.Button(root, text='3', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button(3))
btn4 = tk.Button(root, text='4', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button(4))
btn5 = tk.Button(root, text='5', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button(5))
btn6 = tk.Button(root, text='6', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button(6))
btn7 = tk.Button(root, text='7', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button(7))
btn8 = tk.Button(root, text='8', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button(8))
btn9 = tk.Button(root, text='9', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button(9))
btn0 = tk.Button(root, text='0', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button(0))

btn_add = tk.Button(root, text='+', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button('+'))
btn_sub = tk.Button(root, text='-', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button('-'))
btn_mul = tk.Button(root, text='*', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button('*'))
btn_div = tk.Button(root, text='/', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button('/'))

btn_equal = tk.Button(root, text='=', padx=20, pady=20, font=('Arial', 18), command=calculate)
btn_clear = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=clear)

# Organizar los botones en la cuadrícula
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn_div.grid(row=1, column=3)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn_mul.grid(row=2, column=3)

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn_sub.grid(row=3, column=3)

btn0.grid(row=4, column=0)
btn_clear.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)
btn_add.grid(row=4, column=3)

# Ejecutar el loop principal de la GUI
root.mainloop()
