#Probelma 07. Implimenación de clase punto
import math

# Clase Punto
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "I Cuadrante"
        elif self.x < 0 and self.y > 0:
            return "II Cuadrante"
        elif self.x < 0 and self.y < 0:
            return "III Cuadrante"
        elif self.x > 0 and self.y < 0:
            return "IV Cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "Sobre el origen"

    def vector(self, otro_punto):
        vector_resultante = (otro_punto.x - self.x, otro_punto.y - self.y)
        return f"Vector resultante: {vector_resultante}"

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)

# Clase Rectangulo
class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        return self.base() * self.altura()

def main():
    # Creación de puntos
    A = Punto(2, 3)
    B = Punto(5, 5)
    C = Punto(-3, -1)
    D = Punto(0, 0)

    # Imprimir puntos
    print(f"Punto A: {A}")
    print(f"Punto B: {B}")
    print(f"Punto C: {C}")
    print(f"Punto D: {D}")

    # Consultar cuadrantes
    print(f"El punto A se encuentra en el {A.cuadrante()}")
    print(f"El punto C se encuentra en el {C.cuadrante()}")
    print(f"El punto D se encuentra en el {D.cuadrante()}")

    # Consultar vectores
    print(A.vector(B))
    print(B.vector(A))

    # Consultar distancias (optativo)
    print(f"Distancia entre A y B: {A.distancia(B):.2f}")
    print(f"Distancia entre B y A: {B.distancia(A):.2f}")

    # Determinar el punto más alejado del origen (optativo)
    distancias = {
        "A": A.distancia(D),
        "B": B.distancia(D),
        "C": C.distancia(D)
    }
    mas_lejos = max(distancias, key=distancias.get)
    print(f"El punto más alejado del origen es el punto {mas_lejos}")

    # Crear un rectángulo utilizando los puntos A y B
    rectangulo = Rectangulo(A, B)

    # Consultar base, altura y área del rectángulo
    print(f"Base del rectángulo: {rectangulo.base()}")
    print(f"Altura del rectángulo: {rectangulo.altura()}")
    print(f"Área del rectángulo: {rectangulo.area()}")

if __name__ == "__main__":
    main()