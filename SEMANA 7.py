class Archivo:
    def __init__(self, nombre_archivo):
        """
        Constructor que inicializa el objeto con el nombre de archivo.
        Este constructor simula la apertura de un archivo.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, 'w')
        print(f"Archivo '{self.nombre_archivo}' abierto para escritura.")

    def escribir(self, contenido):
        """
        Método para escribir contenido en el archivo.
        """
        if self.archivo:
            self.archivo.write(contenido)
            print("Contenido escrito en el archivo.")
        else:
            print("Error: el archivo no está abierto.")

    def __del__(self):
        """
        Destructor que se ejecuta cuando el objeto es destruido.
        Cierra el archivo si está abierto.
        """
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado.")
        else:
            print("Error: el archivo no está abierto.")


# Crear una instancia de la clase Archivo
archivo1 = Archivo("ejemplo.txt")

# Escribir contenido en el archivo
archivo1.escribir("Hola, este es un ejemplo de destructor en Python.")

# El archivo se cerrará automáticamente cuando el objeto 'archivo1' sea destruido
del archivo1  # Llamada explícita al destructor para cerrar el archivo
