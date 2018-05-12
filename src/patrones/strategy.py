class UnoEnUno:

    def contar(self,desde,hasta):
        return [x for x in range(desde,hasta)]

class Pares:

    def contar(self,desde,hasta):
        pares = []
        for x in range(desde,hasta):
            if x %2 == 0:
                pares.append(x)
        return pares

class Contador:

    def __init__(self):
        self.__estrategia = UnoEnUno()

    def contar(self,desde,hasta):
        return self.__estrategia.contar(desde,hasta+1)

    def usarEstrategia(self,estrategia):
        self.__estrategia = estrategia


if __name__ == "__main__":

    contador = Contador()
    print(contador.contar(2,10))

    contador.usarEstrategia(Pares())
    print(contador.contar(2, 10))


