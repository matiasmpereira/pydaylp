class CuentaBancaria:

    def __init__(self, numeroDeCuenta, titularCuenta, saldo, tipoCuenta):
        self.__numeroDeCuenta = numeroDeCuenta
        self.__titularCuenta = titularCuenta
        self.__saldo = saldo
        self.__tipoCuenta = tipoCuenta

    def saldo(self):
        return self.__saldo

    def depositar(self,cantidad):
        self.__saldo += cantidad

    def retirar(self,cantidad):

        if self.__tipoCuenta == "cuentaSueldo":
            self.__saldo = self.__saldo - cantidad - 5

        elif self.__tipoCuenta == "cuentaCorriente":
            self.__saldo = self.__saldo - cantidad - 20


if __name__ == "__main__":

    cuentaJose = CuentaBancaria(3410,"Jose Sanchez",100,"cuentaSueldo")
    cuentaJuan = CuentaBancaria(3411,"Juan Perez",100,"cuentaCorriente")

    cuentaJose.retirar(10)
    cuentaJuan.retirar(10)

    print("Saldo Jose: {0}".format(cuentaJose.saldo()))
    print("Saldo JUan: {0}".format(cuentaJuan.saldo()))



