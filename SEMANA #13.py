import tkinter as tk
from tkinter import messagebox

def agregar_dato():
    dato = entrada_texto.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación GUI Básica")
root.geometry("400x300")

# Crear y posicionar los componentes
label = tk.Label(root, text="Ingrese un dato:")
label.pack(pady=5)

entrada_texto = tk.Entry(root, width=40)
entrada_texto.pack(pady=5)

btn_agregar = tk.Button(root, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

lista_datos = tk.Listbox(root, width=50, height=10)
lista_datos.pack(pady=5)

btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
