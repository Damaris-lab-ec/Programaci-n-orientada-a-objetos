class Pokemon:

    def __init__(self, nombre, tipo, nivel, voltaje_max, amperaje_max, color):
         self.nombre = nombre
         self.tipo = tipo
         self.nivel = nivel
         self.voltaje_max = voltaje_max
         self.amperaje_max = amperaje_max
         self.color = color

    def atacar(self):
        print(f"{self.nombre} ataca con impactrueno!!")

    def correr(self):
        print(f"{self.nombre} corre!!")



class Acuatico(Pokemon):

    def __init__(self, nombre, tipo, nivel, voltaje_max, amperaje_max, color, acuatico):
        super().__init__(nombre, tipo, nivel, voltaje_max, amperaje_max, color)
        self.acuatico = acuatico

    def is_acuatico(self):
        if self.acuatico:
            print(f"{self.nombre} is acuatico")
        else:
            print(f"{self.nombre} no es acuatico")


# acua = Acuatico("skuak")


pikachu = Pokemon("Pikachu", "Electrico", 90, 100, 100, "amarillo")

acu = Acuatico("Squirtle", "Agua", 100, 100, 190, "azul", True)


print(pikachu.nombre)
print(pikachu.tipo)
print(pikachu.nivel)
