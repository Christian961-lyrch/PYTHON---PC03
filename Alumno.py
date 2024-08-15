# problema5.py

class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.nota = None

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.nota is not None:
            print(f"Nota: {self.nota}")

    def setAge(self, edad):
        if edad <= 0:
            raise ValueError("La edad debe ser un número positivo.")
        self.edad = edad

    def setNota(self, nota):
        if nota < 0 or nota > 100:
            raise ValueError("La nota debe estar entre 0 y 100.")
        self.nota = nota

def main():
    alumno = Alumno("Juan Pérez", "A12345")

    # Asignar y mostrar la información del alumno
    alumno.display()

    try:
        # Asignar edad
        edad = int(input("Ingrese la edad del alumno: "))
        alumno.setAge(edad)

        # Asignar nota
        nota = float(input("Ingrese la nota del alumno: "))
        alumno.setNota(nota)

        # Mostrar la información actualizada del alumno
        alumno.display()
    
    except ValueError as e:
        print(f"Error: {e}. Intente de nuevo.")

if __name__ == "__main__":
    main()