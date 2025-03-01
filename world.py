# Hola Mundo - Ejemplo básico de un programa en Python

# Esta función saluda al usuario
def saludo():
    print("¡Hola Mundo!")

# Esta función pide el nombre del usuario
def pedir_nombre():
    nombre = input("¿Cómo te llamas? ")
    return nombre

# Esta función saluda al usuario por su nombre
def saludo_personalizado(nombre):
    print(f"Hola {nombre}, ¡bienvenido al programa!")

# Esta función muestra algunas operaciones básicas
def operaciones_basicas():
    print("Haciendo operaciones básicas:")
    a = 10
    b = 5
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    
    print(f"{a} + {b} = {suma}")
    print(f"{a} - {b} = {resta}")
    print(f"{a} * {b} = {multiplicacion}")
    print(f"{a} / {b} = {division}")

# Función principal que organiza el flujo del programa
def main():
    saludo()  # Saludo inicial
    nombre_usuario = pedir_nombre()  # Pedir nombre
    saludo_personalizado(nombre_usuario)  # Saludo personalizado
    operaciones_basicas()  # Mostrar operaciones
    print("Programa terminado.")  # Mensaje final

# Ejecuta la función principal
if __name__ == "__main__":
    main()
