import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Vacía", "Por favor, escribe una tarea antes de añadirla.")

def mark_completed(event=None):
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)
        task_listbox.delete(selected_index)
        task_listbox.insert(selected_index, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Selección Inválida", "Por favor, selecciona una tarea para marcar como completada.")

def delete_task(event=None):
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Selección Inválida", "Por favor, selecciona una tarea para eliminar.")

def close_app(event=None):
    root.destroy()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x400")

# Campo de entrada
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task)  # Atajo para añadir tareas

# Lista de tareas
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Botones
btn_frame = tk.Frame(root)
btn_frame.pack()

add_btn = tk.Button(btn_frame, text="Añadir Tarea", command=add_task)
add_btn.pack(side=tk.LEFT, padx=5)

complete_btn = tk.Button(btn_frame, text="Marcar Completada", command=mark_completed)
complete_btn.pack(side=tk.LEFT, padx=5)

delete_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=delete_task)
delete_btn.pack(side=tk.LEFT, padx=5)

# Atajos de teclado
root.bind("<c>", mark_completed)  # 'C' para marcar completada
root.bind("<d>", delete_task)  # 'D' para eliminar tarea
root.bind("<Delete>", delete_task)  # Tecla 'Delete' para eliminar tarea
root.bind("<Escape>", close_app)  # 'Escape' para cerrar la aplicación

root.mainloop()
