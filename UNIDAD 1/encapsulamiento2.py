#encapsulamiento

class CuentaBancaria:
    def __init__(self, saldo_general):
        self.__saldo =saldo_general

    def depositar(self, cantidad):
         self.__saldo +=valor  ##saldo= saldo + valor


    def retirar(self, valor):
        self.__saldo -=valor


    def obtener_saldo(self):
        return self.__saldo

# creo la insta
mi_cuenta =CuentaBancaria(1000)
print(mi_cuenta.obtener_saldo())

mi_cuenta.retirar(10)
print(mi_cuenta.obtener_saldo())
