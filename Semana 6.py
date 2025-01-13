# Clase base "Vehiculo"
class Vehiculo:
    def __init__(self, marca):
        self.__marca = marca  # Atributo privado (encapsulado)

    def get_marca(self):
        return self.__marca

    def mover(self):
        raise NotImplementedError("Este método debe ser sobrescrito.")

# Clase derivada "Coche"
class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

    def mover(self):
        return f"El coche {self.get_marca()} {self.modelo} está moviéndose."

# Clase derivada "Bicicleta"
class Bicicleta(Vehiculo):
    def __init__(self, marca, tipo):
        super().__init__(marca)
        self.tipo = tipo

    def mover(self):
        return f"La bicicleta {self.get_marca()} de tipo {self.tipo} está pedaleando."

# Creación de instancias y demostración de polimorfismo
vehiculos = [Coche("Toyota", "Corolla"), Bicicleta("Giant", "Montaña")]

for vehiculo in vehiculos:
    print(vehiculo.mover())
