class CuentaBancaria:

    def __init__(self, numeroCuenta, titularCuenta, saldo):
        self.__numeroCuenta = numeroCuenta
        self.__titularCuenta = titularCuenta
        self._saldo = saldo

    def saldo(self):
        return self._saldo

    def depositar(self, cantidad):
        self._saldo += cantidad

    def retirar(self,cantidad):
        self._saldo = self._saldo - cantidad

class CuentaSueldo(CuentaBancaria):

    def retirar(self, cantidad):
        self._saldo = self._saldo - cantidad - 5

class CuentaCorriente(CuentaBancaria):

    def retirar(self, cantidad):
        self._saldo = self._saldo - cantidad - 20

if __name__ == "__main__":

    cuentaJose = CuentaSueldo(3410,"Jose Sanchez",100)
    cuentaJuan = CuentaCorriente(3411,"Juan Perez",100)

    cuentaJose.retirar(10)
    cuentaJuan.retirar(10)

    print("Saldo Jose: {0}".format(cuentaJose.saldo()))
    print("Saldo Juan: {0}".format(cuentaJuan.saldo()))


