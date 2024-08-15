# archivo unico llamado operaciones_y_calculos.py

def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Tipo de dato no válido."

def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Tipo de dato no válido."

def producto(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Tipo de dato no válido."

def division(a, b):
    try:
        return a / b
    except TypeError:
        return "Error: Tipo de dato no válido."
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero."

def main():
    # Ejemplos de operaciones
    print("Suma de 10 y 5:", suma(10, 5))
    print("Resta de 10 y 5:", resta(10, 5))
    print("Producto de 10 y 5:", producto(10, 5))
    print("División de 10 y 5:", division(10, 5))

    # Ejemplos de manejo de errores
    print("Intento de división por cero:", division(10, 0))
    print("Intento de operación con un tipo de dato no válido (suma):", suma(10, "cinco"))
    print("Intento de operación con un tipo de dato no válido (producto):", producto(10, "cinco"))

if __name__ == "__main__":
    main()