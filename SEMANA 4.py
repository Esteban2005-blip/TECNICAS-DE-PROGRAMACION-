# Archivo: sistema_reservas.py

# Clase que representa una habitación de hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        """
        Inicializa una habitación con su número, tipo y precio.
        :param numero: Número de la habitación.
        :param tipo: Tipo de habitación (Ej: 'simple', 'doble', 'suite').
        :param precio: Precio por noche de la habitación.
        """
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False  # Estado de la habitación (disponible o no)

    def reservar(self):
        """Marca la habitación como ocupada."""
        if not self.ocupada:
            self.ocupada = True
            print(f"Habitación {self.numero} reservada con éxito.")
        else:
            print(f"La habitación {self.numero} ya está ocupada.")

    def liberar(self):
        """Marca la habitación como disponible."""
        if self.ocupada:
            self.ocupada = False
            print(f"Habitación {self.numero} liberada con éxito.")
        else:
            print(f"La habitación {self.numero} ya está disponible.")

    def __str__(self):
        """Representación en texto de la habitación."""
        estado = "Ocupada" if self.ocupada else "Disponible"
        return f"Habitación {self.numero} - Tipo: {self.tipo} - Precio: ${self.precio} - Estado: {estado}"


# Clase que representa el sistema de reservas del hotel
class Hotel:
    def __init__(self, nombre):
        """
        Inicializa un hotel con su nombre y una lista de habitaciones vacía.
        :param nombre: Nombre del hotel.
        """
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        """Agrega una habitación al hotel."""
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        """Muestra todas las habitaciones y su estado."""
        print(f"Estado de las habitaciones en el Hotel {self.nombre}:")
        for habitacion in self.habitaciones:
            print(habitacion)

    def buscar_habitacion_disponible(self, tipo):
        """
        Busca la primera habitación disponible del tipo especificado.
        :param tipo: Tipo de habitación deseada.
        :return: La habitación encontrada o None si no hay disponibles.
        """
        for habitacion in self.habitaciones:
            if habitacion.tipo == tipo and not habitacion.ocupada:
                return habitacion
        return None


# Función principal para interactuar con el sistema
def main():
    # Crear un hotel
    hotel = Hotel("Hotel Python")

    # Agregar habitaciones al hotel
    hotel.agregar_habitacion(Habitacion(101, "simple", 50))
    hotel.agregar_habitacion(Habitacion(102, "doble", 80))
    hotel.agregar_habitacion(Habitacion(103, "suite", 150))

    # Mostrar habitaciones disponibles
    hotel.mostrar_habitaciones()

    # Reservar una habitación
    print("\nIntentando reservar una habitación 'doble'...")
    habitacion = hotel.buscar_habitacion_disponible("doble")
    if habitacion:
        habitacion.reservar()
    else:
        print("No hay habitaciones disponibles del tipo solicitado.")


