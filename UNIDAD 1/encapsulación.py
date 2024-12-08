class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print("Depósito realizado con éxito.")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print("Retiro realizado con éxito.")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def obtener_saldo(self):
        return self.__saldo

    def obtener_titular(self):
        return self.__titular

# Creando una instancia de la clase
cuenta = CuentaBancaria("Juan Pérez", 1000)

# Accediendo a los métodos (forma correcta)
cuenta.depositar(500)
print("Saldo actual:", cuenta.obtener_saldo())
cuenta.retirar(200)
print("Titular de la cuenta:", cuenta.obtener_titular())

# Intentando acceder directamente a los atributos (no recomendado)
# Esto generará un error, ya que los atributos están encapsulados
# print(cuenta.__saldo)  # AttributeError