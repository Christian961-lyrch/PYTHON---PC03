#Problema 3. CIRCULO

import math

class CIRCULO:
    def __init__(self, radio):
        """
        Inicializa la clase CIRCULO con el atributo radio.
        """
        self.radio = radio

    def calcular_area(self):
        """
        Calcula el área del círculo usando el radio.
        Retorna el área del círculo.
        """
        return math.pi * (self.radio ** 2)

from circulo import CIRCULO

def main():
    try:
        # Crear el primer objeto de tipo CIRCULO
        radio1 = float(input("Ingrese el radio del primer círculo: "))
        circulo1 = CIRCULO(radio1)
        area1 = circulo1.calcular_area()
        print(f"El área del primer círculo con radio {circulo1.radio} es: {area1:.2f}")

        # Crear el segundo objeto de tipo CIRCULO
        radio2 = float(input("Ingrese el radio del segundo círculo: "))
        circulo2 = CIRCULO(radio2)
        area2 = circulo2.calcular_area()
        print(f"El área del segundo círculo con radio {circulo2.radio} es: {area2:.2f}")
    
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido para el radio.")

if __name__ == "__main__":
    main()