import tkinter as tk
import math

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
        equation.set("Syntax Error")
        expression = ""

# Función para calcular el factorial sin usar la librería math
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_factorial():
    global expression
    try:
        num = int(expression)
        result = str(factorial(num))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Función para calcular el porcentaje
def calculate_percentage():
    global expression
    try:
        result = str(eval(expression) / 100)
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Función para calcular el exponente sin usar math.pow
def calculate_exponent():
    global expression
    try:
        # Reemplazar el operador '^' por '**' en la expresión
        if '^' in expression:
            base, exponent = map(int, expression.split('^'))
            result = str(base ** exponent)
        else:
            result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Función para calcular la raíz cuadrada usando math
def calculate_sqrt():
    global expression
    try:
        result = str(math.sqrt(float(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Función para calcular el valor absoluto usando math
def calculate_abs():
    global expression
    try:
        result = str(abs(float(expression)))
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
screen = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=20, borderwidth=4)
screen.grid(row=0, column=0, columnspan=5)

# Crear labels para conversiones de números
label_hex = tk.Label(root, font=('Arial', 14), text='Hex:')
label_dec = tk.Label(root, font=('Arial', 14), text='Dec:')
label_oct = tk.Label(root, font=('Arial', 14), text='Oct:')
label_bin = tk.Label(root, font=('Arial', 14), text='Bin:')

label_hex.grid(row=1, column=0, sticky='e')
label_dec.grid(row=2, column=0, sticky='e')
label_oct.grid(row=3, column=0, sticky='e')
label_bin.grid(row=4, column=0, sticky='e')

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

# Botones para letras hexadecimales
btnA = tk.Button(root, text='A', padx=20, pady=20, font=('Arial', 18))
btnB = tk.Button(root, text='B', padx=20, pady=20, font=('Arial', 18))
btnC = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18))
btnD = tk.Button(root, text='D', padx=20, pady=20, font=('Arial', 18))
btnE = tk.Button(root, text='E', padx=20, pady=20, font=('Arial', 18))
btnF = tk.Button(root, text='F', padx=20, pady=20, font=('Arial', 18))

# Botones para operaciones matemáticas
btn_add = tk.Button(root, text='+', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button('+'))
btn_sub = tk.Button(root, text='-', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button('-'))
btn_mul = tk.Button(root, text='*', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button('*'))
btn_div = tk.Button(root, text='/', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button('/'))

# Botones para funciones científicas
btn_log = tk.Button(root, text='log', padx=20, pady=20, font=('Arial', 18))
btn_por = tk.Button(root, text='%', padx=20, pady=20, font=('Arial', 18), command=calculate_percentage)
btn_raiz = tk.Button(root, text='√', padx=20, pady=20, font=('Arial', 18), command=calculate_sqrt)
btn_fact = tk.Button(root, text='n!', padx=20, pady=20, font=('Arial', 18), command=calculate_factorial)
btn_arri = tk.Button(root, text='^', padx=20, pady=20, font=('Arial', 18), command=lambda: press_button('**'))
btn_back = tk.Button(root, text='←', padx=20, pady=20, font=('Arial', 18))
btn_abs = tk.Button(root, text='ABS', padx=20, pady=20, font=('Arial', 18), command=calculate_abs)
btn_deci = tk.Button(root, text='.', padx=20, pady=20, font=('Arial', 18))

btn_equal = tk.Button(root, text='=', padx=20, pady=20, font=('Arial', 18), command=calculate)
btn_clear = tk.Button(root, text='CE', padx=20, pady=20, font=('Arial', 18), command=clear)

# Organizar los botones en la cuadrícula
# Row = 1, column = n
btnA.grid(row=5, column=0)
btn_log.grid(row=5, column=1)
btn_por.grid(row=5, column=2)
btn_clear.grid(row=5, column=3)
btn_back.grid(row=5, column=4)

# Row = 2, column = n
btnB.grid(row=6, column=0)
btn_raiz.grid(row=6, column=1)
btn_arri.grid(row=6, column=2)
btn_fact.grid(row=6, column=3)
btn_div.grid(row=6, column=4)

# Row = 3, column = n
btnC.grid(row=7, column=0)
btn7.grid(row=7, column=1)
btn8.grid(row=7, column=2)
btn9.grid(row=7, column=3)
btn_mul.grid(row=7, column=4)

# Row = 4, column = n
btnD.grid(row=8, column=0)
btn4.grid(row=8, column=1)
btn5.grid(row=8, column=2)
btn6.grid(row=8, column=3)
btn_sub.grid(row=8, column=4)

# Row = 5, column = n
btnE.grid(row=9, column=0)
btn1.grid(row=9, column=1)
btn2.grid(row=9, column=2)
btn3.grid(row=9, column=3)
btn_add.grid(row=9, column=4)

# Row = 6, column = n
btnF.grid(row=10, column=0)
btn_abs.grid(row=10, column=1)
btn0.grid(row=10, column=2)
btn_deci.grid(row=10, column=3)
btn_equal.grid(row=10, column=4)

# Iniciar el bucle principal de la aplicación
root.mainloop()
