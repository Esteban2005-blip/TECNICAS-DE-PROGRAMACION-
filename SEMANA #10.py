import os
import json

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde un archivo de texto."""
        if not os.path.exists(self.archivo):
            print("[INFO] Archivo de inventario no encontrado. Se creará uno nuevo.")
            return
        try:
            with open(self.archivo, "r") as f:
                self.productos = json.load(f)
                print("[INFO] Inventario cargado correctamente.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("[ERROR] No se pudo cargar el inventario. El archivo puede estar vacío o corrupto.")
        except PermissionError:
            print("[ERROR] No tienes permisos para leer el archivo de inventario.")

    def guardar_inventario(self):
        """Guarda el inventario en un archivo de texto."""
        try:
            with open(self.archivo, "w") as f:
                json.dump(self.productos, f, indent=4)
                print("[INFO] Inventario guardado correctamente.")
        except PermissionError:
            print("[ERROR] No tienes permisos para escribir en el archivo de inventario.")

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un nuevo producto o actualiza la cantidad si ya existe."""
        if nombre in self.productos:
            self.productos[nombre]['cantidad'] += cantidad
        else:
            self.productos[nombre] = {'cantidad': cantidad, 'precio': precio}
        self.guardar_inventario()
        print(f"[INFO] Producto '{nombre}' agregado/actualizado correctamente.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"[INFO] Producto '{nombre}' eliminado correctamente.")
        else:
            print(f"[ERROR] Producto '{nombre}' no encontrado en el inventario.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("[INFO] El inventario está vacío.")
            return
        print("\n[INVENTARIO ACTUAL]")
        for nombre, datos in self.productos.items():
            print(f"- {nombre}: {datos['cantidad']} unidades - ${datos['precio']} cada uno")

# Interfaz de usuario en consola
def menu():
    inventario = Inventario()
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIOS ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "3":
            inventario.mostrar_inventario()
        elif opcion == "4":
            print("[INFO] Saliendo del sistema.")
            break
        else:
            print("[ERROR] Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
