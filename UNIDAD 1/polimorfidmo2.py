#Polimorfismo

class Semana:
  def __init__(self):
    self.temperaturas = []

  def ingresar_temperaturas(self):
    for dia in range(1, 8):
      temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
      self.temperaturas.append(temperatura)

  def calcular_promedio(self):
    suma = sum(self.temperaturas)
    promedio = suma / len(self.temperaturas)
    return promedio

# Creación de un objeto de la clase Semana
semana = Semana()
semana.ingresar_temperaturas()
promedio = semana.calcular_promedio()
print("El promedio semanal de temperaturas es:", promedio)