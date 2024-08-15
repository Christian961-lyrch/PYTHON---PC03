# problema2. NOTAS.py

def funcion_notas():
    """
    Solicita una lista de calificaciones separadas por comas al usuario.
    Devuelve la lista de calificaciones convertidas a enteros.
    """
    while True:
        try:
            # Solicitar la entrada del usuario
            notas = input("Ingrese una lista de calificaciones separadas por comas: ")
            
            # Dividir la cadena en calificaciones individuales
            lista_notas = notas.split(',')
            
            # Convertir cada calificación en un entero y almacenar en una nueva lista
            notas = [int(nota.strip()) for nota in lista_notas]
            
            return notas
        
        except ValueError:
            print("Error: Asegúrese de que todos los valores sean números enteros separados por comas.")

# main2.py

from Notas import funcion_notas

def main():
    notas = funcion_notas()
    print("Las calificaciones ingresadas son:", notas)

if __name__ == "__main__":
    main()