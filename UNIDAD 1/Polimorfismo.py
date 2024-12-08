class Forma:
    def area(self):
        pass  # Método abstracto

class Rectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio**2

# Creando objetos
formas = [Rectangulo(5, 4), Circulo(3)]

for forma in formas:
    print(f"El área de la forma es: {forma.area()}")