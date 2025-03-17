import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()
    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        entry_fecha.set_date(entry_fecha.get_date())
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")

def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        confirmar = messagebox.askyesno("Confirmar eliminación", "¿Seguro que desea eliminar este evento?")
        if confirmar:
            tree.delete(selected_item)
    else:
        messagebox.showwarning("Seleccionar evento", "Seleccione un evento para eliminar.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Frame para la entrada de datos
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

# Etiquetas y campos de entrada
lbl_fecha = tk.Label(frame_input, text="Fecha:")
lbl_fecha.grid(row=0, column=0, padx=5, pady=5)
entry_fecha = DateEntry(frame_input, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

lbl_hora = tk.Label(frame_input, text="Hora:")
lbl_hora.grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_input)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

lbl_descripcion = tk.Label(frame_input, text="Descripción:")
lbl_descripcion.grid(row=2, column=0, padx=5, pady=5)
entry_descripcion = tk.Entry(frame_input)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Botones
btn_agregar = tk.Button(root, text="Agregar Evento", command=agregar_evento)
btn_agregar.pack(pady=5)

btn_eliminar = tk.Button(root, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.pack(pady=5)

btn_salir = tk.Button(root, text="Salir", command=root.quit)
btn_salir.pack(pady=5)

# TreeView para mostrar eventos
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

root.mainloop()
