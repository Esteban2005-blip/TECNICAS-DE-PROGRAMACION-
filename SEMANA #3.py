# Programación Tradicional

def ingresar_temperaturas():
    """Función para ingresar temperaturas diarias."""
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingresa la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Función para calcular el promedio de las temperaturas."""
    return sum(temperaturas) / len(temperaturas)

def main_tradicional():
    """Función principal para la programación tradicional."""
    print("--- Programación Tradicional ---")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")

main_tradicional()

# Programación Orientada a Objetos (POO)

class ClimaDiario:
    """Clase que representa la información diaria del clima."""
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """Método para ingresar temperaturas diarias."""
        for i in range(7):
            temp = float(input(f"Ingresa la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """Método para calcular el promedio semanal de temperaturas."""
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

def main_poo():
    """Función principal para la programación orientada a objetos."""
    print("--- Programación Orientada a Objetos ---")
    clima = ClimaDiario()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")

main_poo()
