import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {"ID": self.id_producto, "Nombre": self.nombre, "Cantidad": self.cantidad, "Precio": self.precio}


class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            return True
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_en_archivo()
            return True
        return False

    def buscar_producto(self, nombre):
        return [p.to_dict() for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def mostrar_productos(self):
        return [p.to_dict() for p in self.productos.values()]

    def guardar_en_archivo(self):
        with open("inventario.json", "w") as f:
            json.dump([p.to_dict() for p in self.productos.values()], f)

    def cargar_desde_archivo(self):
        try:
            with open("inventario.json", "r") as f:
                datos = json.load(f)
                self.productos = {p["ID"]: Producto(p["ID"], p["Nombre"], p["Cantidad"], p["Precio"]) for p in datos}
        except FileNotFoundError:
            self.productos = {}


def menu():
    inventario = Inventario()
    while True:
        print("\nGestión de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
            print("Producto agregado.")
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            if inventario.eliminar_producto(id_producto):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje vacío para no cambiar): ")
            precio = input("Nuevo precio (deje vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            if inventario.actualizar_producto(id_producto, cantidad, precio):
                print("Producto actualizado.")
            else:
                print("Producto no encontrado.")
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            print(resultados if resultados else "No se encontraron productos.")
        elif opcion == "5":
            print(inventario.mostrar_productos())
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
