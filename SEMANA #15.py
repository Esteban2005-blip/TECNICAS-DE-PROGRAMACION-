import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía")

def mark_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task_text = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(selected_task_index, f"✔ {task_text}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")

def on_enter_pressed(event):
    add_task()

# Crear ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Campo de entrada y botón para añadir tarea
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)
entry_task.bind("<Return>", on_enter_pressed)

btn_add = tk.Button(root, text="Añadir Tarea", command=add_task)
btn_add.pack()

# Listbox para mostrar tareas
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)

# Botones para marcar como completada y eliminar
btn_complete = tk.Button(root, text="Marcar como Completada", command=mark_completed)
btn_complete.pack()

btn_delete = tk.Button(root, text="Eliminar Tarea", command=delete_task)
btn_delete.pack()

# Ejecutar la aplicación
root.mainloop()
