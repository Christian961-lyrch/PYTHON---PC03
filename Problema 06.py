# problema6.py

class Producto:
    def __init__(self, codigo, nombre, precio, año_fabricacion, marca):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.año_fabricacion = año_fabricacion
        self.marca = marca

    def __str__(self):
        return (f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: ${self.precio:.2f}, "
                f"Año: {self.año_fabricacion}, Marca: {self.marca}")

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el catálogo.")
        else:
            for producto in self.productos:
                print(producto)

    def filtrar_por_año(self, año):
        print(f"Productos fabricados en {año}:")
        filtrados = [p for p in self.productos if p.año_fabricacion == año]
        if not filtrados:
            print(f"No se encontraron productos del año {año}.")
        else:
            for producto in filtrados:
                print(producto)

    def filtrar_por_marca(self, marca):
        print(f"Productos de la marca {marca}:")
        filtrados = [p for p in self.productos if p.marca.lower() == marca.lower()]
        if not filtrados:
            print(f"No se encontraron productos de la marca {marca}.")
        else:
            for producto in filtrados:
                print(producto)

def main():
    # Crear catálogo
    catalogo = Catalogo()

    # Crear productos
    producto1 = Producto("A123", "Filtro de aceite", 15.50, 2022, "Bosch")
    producto2 = Producto("B456", "Batería de auto", 120.00, 2021, "Exide")
    producto3 = Producto("C789", "Bujía", 7.25, 2023, "NGK")

    # Agregar productos al catálogo
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    # Mostrar todos los productos
    print("Catálogo completo:")
    catalogo.mostrar_productos()

    # Filtrar productos por año de fabricación
    print("\nFiltrar productos por año 2022:")
    catalogo.filtrar_por_año(2022)

    # Filtrar productos por marca
    print("\nFiltrar productos por marca 'Bosch':")
    catalogo.filtrar_por_marca("Bosch")

if __name__ == "__main__":
    main()