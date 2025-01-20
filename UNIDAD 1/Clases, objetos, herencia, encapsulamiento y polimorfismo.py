# Clase base Animal
class Animal:
    # Atributo privado, solo accesible dentro de la clase
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo encapsulado
        self.edad = edad  # Atributo público

    # Método público
    def hablar(self):
        return f"Este animal hace un sonido."

    # Método para acceder a un atributo privado
    def obtener_nombre(self):
        return self.__nombre

    # Método para establecer un atributo privado
    def establecer_nombre(self, nombre):
        self.__nombre = nombre

# Clase derivada Perro, que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.raza = raza  # Atributo específico de la clase Perro

    # Sobrescritura del método hablar (polimorfismo)
    def hablar(self):
        return f"{self.obtener_nombre()} dice: ¡Guau, guau!"

    # Método adicional específico de la clase Perro
    def mostrar_raza(self):
        return f"{self.obtener_nombre()} es de raza {self.raza}."

# Clase derivada Gato, que también hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color  # Atributo específico de la clase Gato

    # Sobrescritura del método hablar (polimorfismo)
    def hablar(self):
        return f"{self.obtener_nombre()} dice: ¡Miau!"

    # Método adicional específico de la clase Gato
    def mostrar_color(self):
        return f"{self.obtener_nombre()} es de color {self.color}."

# Creación de instancias de las clases
perro = Perro("Oddy", 5, "Criolla")
gato = Gato("Miau", 3, "Blanco")

# Mostrar información sobre el perro
print(perro.hablar())  # Polimorfismo: el perro tiene su propia implementación de hablar
print(perro.mostrar_raza())

# Mostrar información sobre el gato
print(gato.hablar())  # Polimorfismo: el gato tiene su propia implementación de hablar
print(gato.mostrar_color())

# Ejemplo de uso de métodos encapsulados
print(f"El nombre del perro es: {perro.obtener_nombre()}")
perro.establecer_nombre("Max")  # Cambiar el nombre del perro
print(f"El nuevo nombre del perro es: {perro.obtener_nombre()}")
