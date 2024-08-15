# problema 01. GASOLINA.py

def porcentaje_gasolina(X, Y):
    """
    Calcula el porcentaje de combustible basado en la fracción X/Y.
    """
    try:
        # Verificar que Y no sea cero para evitar división por cero
        if Y == 0:
            raise ZeroDivisionError
        
        # Verificar que X sea menor o igual a Y
        if X > Y:
            raise ValueError("X no puede ser mayor que Y")
        
        # Calcular el porcentaje
        percentage = (X / Y) * 100
        
        # Determinar la salida según el porcentaje
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return f"{round(percentage)}%"
    
    except ZeroDivisionError:
        raise ZeroDivisionError("Y no puede ser cero.")
    except ValueError as ve:
        raise ValueError(f"Error: {ve}")

def fraccion_gasolina():
    """
    Pide al usuario la fracción de combustible  y la imprime como enteros X e Y.
    """
    while True:
        try:
            # Solicitar la entrada del usuario
            fraction = input("Ingrese la fracción de combustible (X/Y): ")
            
            # Separar la entrada en X e Y
            X, Y = fraction.split('/')
            
            # Convertir X e Y a enteros
            X = int(X)
            Y = int(Y)
            
            return X, Y
        
        except ValueError:
            print("Error: X y Y deben ser números enteros, y X debe ser menor o igual a Y.")

# main01.py

from gasolina import porcentaje_gasolina, fraccion_gasolina

def main():
    while True:
        try:
            # Obtener los valores X e Y
            X, Y = fraccion_gasolina()
            
            # Calcular el porcentaje de combustible
            result = porcentaje_gasolina(X, Y)
            
            # Imprimir el resultado
            print("Output:", result)
            break  # Terminar el bucle si todo es correcto
        
        except (ZeroDivisionError, ValueError) as e:
            print(e)
            print("Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
