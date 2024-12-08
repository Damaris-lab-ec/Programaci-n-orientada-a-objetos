class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print("El vehículo está arrancando.")

class Coche(Vehiculo):
    def abrir_techo_solar(self):
        print("Abriendo techo solar.")

class Moto(Vehiculo):
    def hacer_wheelie(self):
        print("Haciendo un wheelie.")

mi_coche = Coche("Mazda", "Serie 3")
mi_moto = Moto("Harley Davidson", "Sportster")

mi_coche.arrancar()
mi_coche.abrir_techo_solar()
mi_moto.arrancar()
mi_moto.hacer_wheelie()
