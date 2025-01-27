import os
import subprocess

def leer_codigo(ruta_script):
    """Lee y muestra el código de un archivo dado."""
    ruta_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Contenido de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def correr_script(ruta_script):
    """Ejecuta un script en una terminal según el sistema operativo."""
    try:
        comando = ['cmd', '/k', 'python', ruta_script] if os.name == 'nt' else ['xterm', '-hold', '-e', 'python3', ruta_script]
        subprocess.Popen(comando)
    except Exception as e:
        print(f"Error al ejecutar el script: {e}")

def menu_principal():
    """Muestra el menú principal y permite la navegación entre unidades."""
    ruta_base = os.getcwd()  # Cambiado para usar el directorio actual en lugar de __file__
    unidades = {'1': 'Unidad_1', '2': 'Unidad_2'}

    while True:
        print("\nDashboard - Menú Principal")
        for key, nombre in unidades.items():
            print(f"{key} - {nombre}")
        print("0 - Salir")

        eleccion = input("Selecciona una opción: ")
        if eleccion == '0':
            print("Saliendo del programa.")
            break
        elif eleccion in unidades:
            submenu(os.path.join(ruta_base, unidades[eleccion]))
        else:
            print("Opción no válida, intenta de nuevo.")

def submenu(ruta_unidad):
    """Muestra un submenú con las subcarpetas disponibles."""
    subcarpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú - Subcarpetas")
        for idx, carpeta in enumerate(subcarpetas, 1):
            print(f"{idx} - {carpeta}")
        print("0 - Volver al menú principal")

        eleccion = input("Selecciona una opción: ")
        if eleccion == '0':
            break
        try:
            idx = int(eleccion) - 1
            if 0 <= idx < len(subcarpetas):
                lista_scripts(os.path.join(ruta_unidad, subcarpetas[idx]))
            else:
                print("Selección inválida.")
        except ValueError:
            print("Por favor, introduce un número válido.")

def lista_scripts(ruta_subcarpeta):
    """Lista los scripts disponibles y permite ejecutar o ver su contenido."""
    scripts = [f.name for f in os.scandir(ruta_subcarpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\nScripts Disponibles")
        for idx, script in enumerate(scripts, 1):
            print(f"{idx} - {script}")
        print("0 - Volver al submenú")

        eleccion = input("Elige un script: ")
        if eleccion == '0':
            break
        try:
            idx = int(eleccion) - 1
            if 0 <= idx < len(scripts):
                ruta_script = os.path.join(ruta_subcarpeta, scripts[idx])
                codigo = leer_codigo(ruta_script)
                if codigo:
                    ejecutar = input("¿Ejecutar este script? (s/n): ").lower()
                    if ejecutar == 's':
                        correr_script(ruta_script)
                    elif ejecutar == 'n':
                        print("Script no ejecutado.")
                    else:
                        print("Opción no válida.")
            else:
                print("Selección inválida.")
        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    menu_principal()
