class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla para garantizar inmutabilidad
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo_autor[0]} de {self.titulo_autor[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = set()  # Conjunto para manejar IDs de usuario únicos

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' agregado a la biblioteca.")
        else:
            print("Este libro ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            print(f"Usuario {usuario.nombre} registrado con éxito.")
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            self.usuarios.remove(usuario.id_usuario)
            print(f"Usuario {usuario.nombre} dado de baja.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, usuario, isbn):
        if isbn in self.libros:
            usuario.libros_prestados.append(self.libros.pop(isbn))
            print(f"Libro con ISBN {isbn} prestado a {usuario.nombre}.")
        else:
            print("El libro no está disponible o no existe.")

    def devolver_libro(self, usuario, isbn):
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                self.libros[isbn] = libro
                usuario.libros_prestados.remove(libro)
                print(f"Libro con ISBN {isbn} devuelto por {usuario.nombre}.")
                return
        print("El usuario no tiene este libro prestado.")

    def buscar_libro(self, criterio, valor):
        resultados = [str(libro) for libro in self.libros.values() if valor.lower() in str(getattr(libro, criterio)).lower()]
        print("Resultados de búsqueda:")
        print("\n".join(resultados) if resultados else "No se encontraron libros.")

    def listar_libros_prestados(self, usuario):
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")


# Pruebas
biblioteca = Biblioteca()
libro1 = Libro("1984", "George Orwell", "Ficción", "1234567890")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "0987654321")
usuario1 = Usuario("Juan Pérez", "U001")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.registrar_usuario(usuario1)
biblioteca.prestar_libro(usuario1, "1234567890")
biblioteca.listar_libros_prestados(usuario1)
biblioteca.devolver_libro(usuario1, "1234567890")
biblioteca.listar_libros_prestados(usuario1)
