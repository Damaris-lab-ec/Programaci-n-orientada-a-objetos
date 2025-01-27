class Libro:
    # Constructor (__init__)
    def __init__(self, titulo, autor, año_publicacion):
        """
        El constructor se ejecuta cuando se crea una nueva instancia de la clase Libro.
        Inicializa los atributos del libro: título, autor y año de publicación.
        """
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        print(f"Se ha creado el libro '{self.titulo}' de {self.autor}, publicado en {self.año_publicacion}.")

    # Destructor (__del__)
    def __del__(self):
        """
        El destructor se ejecuta cuando la instancia del objeto se destruye o se elimina.
        Aquí realizamos una limpieza simulada mostrando un mensaje al eliminar el libro.
        """
        print(f"Se ha destruido el libro '{self.titulo}'.")


# Creación de objetos (instancias) de la clase Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("1984", "George Orwell", 1949)

# Eliminación explícita de un objeto
del libro1  # Esto desencadenará el destructor para libro1

# El siguiente libro será destruido automáticamente al finalizar el programa,
# ya que el recolector de basura de Python se encarga de ello.
del libro2
