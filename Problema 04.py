# problema4.py

class RECTANGULO:
    def __init__(area, largo, ancho):
        if largo <= 0 or ancho <= 0:
            raise ValueError("Por favor, ingrese valores positivos para el largo el ancho")
        area.largo = largo
        area.ancho = ancho

    def calcular_area(area):
        return area.largo * area.ancho

class CUADRADO(RECTANGULO):
    def __init__(area, lado):
        super().__init__(lado, lado)

def main():
    try:
        largo = float(input("Ingrese el largo del rectángulo. Sea un número positivo: "))
        ancho = float(input("Ingrese el ancho del rectángulo. Sea un número positivo: "))
        rectangulo = RECTANGULO(largo, ancho)
        print(f"El área del rectángulo es: {rectangulo.calcular_area():.2f}")

        lado = float(input("Ingrese el lado del cuadrado: "))
        cuadrado = CUADRADO(lado)
        print(f"El área del cuadrado es: {cuadrado.calcular_area():.2f}")
    
    except ValueError as e:
        print(f"Error: {e}. Intente de nuevo.")

if __name__ == "__main__":
    main()