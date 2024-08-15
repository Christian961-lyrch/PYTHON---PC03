import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

def validar_entrada_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("El valor debe ser un número positivo.")
            else:
                return valor
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            radio = validar_entrada_float("Ingrese el radio del círculo: ")
            circulo = Circulo(radio)
            print(f"El área del círculo es: {circulo.area():.2f}")

        elif opcion == "2":
            largo = validar_entrada_float("Ingrese el largo del rectángulo: ")
            ancho = validar_entrada_float("Ingrese el ancho del rectángulo: ")
            rectangulo = Rectangulo(largo, ancho)
            print(f"El área del rectángulo es: {rectangulo.area():.2f}")

        elif opcion == "3":
            lado = validar_entrada_float("Ingrese el lado del cuadrado: ")
            cuadrado = Cuadrado(lado)
            print(f"El área del cuadrado es: {cuadrado.area():.2f}")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()