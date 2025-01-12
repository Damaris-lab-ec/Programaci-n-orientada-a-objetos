class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print("Libro prestado.")
        else:
            print("Libro no disponible.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print("Libro devuelto.")
        else:
            print("Libro ya está disponible.")

class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if not libro.prestado:
            self.libros_prestados.append(libro)
            libro.prestar()
            print(f"{self.nombre} ha prestado {libro.titulo}")
        else:
            print("El libro no está disponible.")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

# Ejemplo de uso:
biblioteca = Biblioteca()

libro1 = Libro("Como Agua para Chocolate", "Laura Esquivel Valdés", "978-84-206-0004-3")
libro2 = Libro("El imperio Final", "Brandon Sanderson", "978-84-206-0282-5")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

usuario1 = Usuario("Damaris Lara", "12345678A")

usuario1.prestar_libro(libro1)

libro_encontrado = biblioteca.buscar_libro("1984")
if libro_encontrado:
    usuario1.prestar_libro(libro_encontrado)