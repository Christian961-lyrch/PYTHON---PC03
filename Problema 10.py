class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}"


class GestionBiblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def listar_libros(self):
        if self.libros:
            for libro in self.libros:
                print(libro)
        else:
            print("La biblioteca no tiene libros.")

    def buscar_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros con el título '{titulo}'.")

    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros if autor.lower() in libro.autor.lower()]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros del autor '{autor}'.")


def menu():
    gestion = GestionBiblioteca()

    while True:
        print("\nMenú de Gestión de Biblioteca:")
        print("1. Agregar un libro")
        print("2. Listar todos los libros")
        print("3. Buscar un libro por título")
        print("4. Buscar un libro por autor")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            gestion.agregar_libro(libro)

        elif opcion == "2":
            print("Lista de libros en la biblioteca:")
            gestion.listar_libros()

        elif opcion == "3":
            titulo = input("Ingrese el título a buscar: ")
            gestion.buscar_por_titulo(titulo)

        elif opcion == "4":
            autor = input("Ingrese el autor a buscar: ")
            gestion.buscar_por_autor(autor)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()