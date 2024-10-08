import tkinter as tk
from tkinter import END, messagebox, ttk

# Ruta del archivo donde se guardarán los datos
archivo_datos = 'libros.txt'


def increment_id():
    try:
        with open(archivo_datos, 'r') as archivo:
            lineas = archivo.readlines()
            if lineas:
                ultimo_id = int(lineas[-1].split(',')[0])
                return ultimo_id + 1
            else:
                return 1
    except FileNotFoundError:
        return 1


def new():
    id_actual = increment_id()
    txId.delete(0, END)
    txId.insert(0, id_actual)

    habilitar_componentes()
    btnSalvar['state'] = tk.NORMAL
    btnCancelar['state'] = tk.NORMAL

    btnNew['state'] = tk.DISABLED
    btnEditar['state'] = tk.DISABLED
    btnEliminar['state'] = tk.DISABLED


def save():
    id = txId.get()
    titulo = txTitulo.get()
    autor = txAutor.get()
    editorial = txEditorial.get()
    clasificacion = cbClasificacion.get()

    if id and titulo and autor and editorial and clasificacion:
        try:
            with open(archivo_datos, 'a') as archivo:
                archivo.write(f'{id},{titulo},{autor},{editorial},{clasificacion}\n')

            messagebox.showinfo('Éxito', 'Datos guardados correctamente.')
            cancel()
        except Exception as e:
            messagebox.showerror('Error', f'Error al guardar datos: {e}')
    else:
        messagebox.showerror('Error', 'Rellene los campos faltantes')


def edit():
    btnEditar['state'] = tk.DISABLED
    btnEliminar['state'] = tk.DISABLED
    btnSalvar['state'] = tk.NORMAL
    btnCancelar['state'] = tk.NORMAL
    id = txId.get()
    titulo = txTitulo.get()
    autor = txAutor.get()
    editorial = txEditorial.get()
    clasificacion = cbClasificacion.get()
    with open(archivo_datos, 'a') as archivo:
        #   Tries to delete the data
        if id == txId:
            delete()
            lineas = "libros.txt".readlines()
        #   Try to overwrite the data
        if id and titulo and autor and editorial and clasificacion:
            try:
                with open(archivo_datos, 'a') as archivo:
                    delete()
                    archivo.write(f'{id},{titulo},{autor},{editorial},{clasificacion}\n')
                messagebox.showinfo('Éxito', 'Datos actualizados correctamente.')
                cancel()
            except Exception as e:
                messagebox.showerror('Error', f'Error al actualizar datos: {e}')
        else:
            messagebox.showerror('Error', 'Rellene los campos faltantes')

def delete():
    id_to_delete = searchEntry.get()

    try:
        with open(archivo_datos, 'r+') as archivo:
            lineas = archivo.readlines()
            archivo.seek(0)
            archivo.truncate()

            encontrado = False
            for linea in lineas:
                datos = linea.strip().split(',')
                if datos[0] == id_to_delete:
                    encontrado = True
                else:
                    archivo.write(linea)

            if encontrado:
                messagebox.showinfo('Éxito', 'Registro eliminado correctamente.')
            else:
                messagebox.showerror('Error', 'Registro no encontrado.')

        cancel()
    except Exception as e:
        messagebox.showerror('Error', f'Error al eliminar datos: {e}')


def search():
    id_to_search = searchEntry.get()

    try:
        with open(archivo_datos, 'r') as archivo:
            lineas = archivo.readlines()
            encontrado = False
            for linea in lineas:
                datos = linea.strip().split(',')
                if datos[0] == id_to_search:
                    txId.delete(0, END)
                    txId.insert(0, datos[0])

                    txTitulo.delete(0, END)
                    txTitulo.insert(0, datos[1])

                    txAutor.delete(0, END)
                    txAutor.insert(0, datos[2])

                    txEditorial.delete(0, END)
                    txEditorial.insert(0, datos[3])

                    cbClasificacion.set(datos[4])

                    encontrado = True
                    break

            if encontrado:
                habilitar_componentes()
                btnEditar['state'] = tk.NORMAL
                btnEliminar['state'] = tk.NORMAL
            else:
                messagebox.showerror('Error', 'Registro no encontrado.')
    except FileNotFoundError:
        messagebox.showerror('Error', 'No se encontró el archivo de datos.')


def cancel():
    # Elimina el ID y limpia los campos
    deshabilitar_componentes()

    btnNew['state'] = tk.NORMAL
    btnSalvar['state'] = tk.DISABLED
    btnCancelar['state'] = tk.DISABLED
    btnEditar['state'] = tk.DISABLED
    btnEliminar['state'] = tk.DISABLED


def habilitar_componentes():
    txId['state'] = tk.NORMAL
    txTitulo['state'] = tk.NORMAL
    txAutor['state'] = tk.NORMAL
    txEditorial['state'] = tk.NORMAL
    cbClasificacion['state'] = tk.NORMAL


def deshabilitar_componentes():
    txId.delete(0, END)
    txTitulo.delete(0, END)
    txAutor.delete(0, END)
    txEditorial.delete(0, END)
    cbClasificacion.set('')

    txId['state'] = tk.DISABLED
    txTitulo['state'] = tk.DISABLED
    txAutor['state'] = tk.DISABLED
    txEditorial['state'] = tk.DISABLED
    cbClasificacion['state'] = tk.DISABLED


# Lógica para la ventana
root = tk.Tk()
root.config(width=500, height=400)
root.title("Biblioteca")

searchLabel = ttk.Label(root, text="Ingrese el ID a buscar").place(x=50, y=10)
searchEntry = tk.Entry(root)
searchEntry.place(x=190, y=10)

btnBuscar = tk.Button(root, text="Buscar", command=search, bg='#efc16d'
                                                              '')
btnBuscar.place(x=320, y=10)

tk.Label(root, text="ID:").place(x=10, y=15)
txId = tk.Entry(root, state=tk.DISABLED)
txId.place(x=10, y=30)

tk.Label(root, text="Título Libro").place(x=10, y=55)
txTitulo = tk.Entry(root, width=30, state=tk.DISABLED)
txTitulo.place(x=10, y=70)

tk.Label(root, text="Autor:").place(x=10, y=95)
txAutor = tk.Entry(root, state=tk.DISABLED)
txAutor.place(x=10, y=120)

tk.Label(root, text="Editorial:").place(x=10, y=155)
txEditorial = tk.Entry(root, state=tk.DISABLED)
txEditorial.place(x=10, y=185)

tk.Label(root, text="Clasificación:").place(x=10, y=210)
cbClasificacion = ttk.Combobox(root, state="disabled",
                               values=["Novela", "Cuento", "Finanzas", "Economía"])
cbClasificacion.place(x=10, y=240)

btnNew = tk.Button(root, text="Nuevo", command=new, bg='#efc16d')
btnNew.place(x=40, y=290)

btnSalvar = tk.Button(root, text="Salvar", command=save, state=tk.DISABLED, bg='#efc16d')
btnSalvar.place(x=100, y=290)

btnCancelar = tk.Button(root, text="Cancelar", command=cancel, state=tk.DISABLED, bg='#efc16d')
btnCancelar.place(x=150, y=290)

btnEditar = tk.Button(root, text="Editar", command=edit, state=tk.DISABLED, bg='#efc16d')
btnEditar.place(x=220, y=290)

btnEliminar = tk.Button(root, text="Eliminar", command=delete, state=tk.DISABLED, bg='#efc16d')
btnEliminar.place(x=270, y=290)

root.mainloop()
