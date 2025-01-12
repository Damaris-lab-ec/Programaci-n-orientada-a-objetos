
#Es necesario saber hacer conversiones de temperatura ya que lo necesitamos en la vida cotidiana

def celsius_a_fahrenheit(celsius):
  """Convierte una temperatura en grados Celsius a Fahrenheit.

  Args:
    celsius: Temperatura en grados Celsius.

  Returns:
    La temperatura equivalente en grados Fahrenheit.
  """

  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# Ejemplo de uso:
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit}")