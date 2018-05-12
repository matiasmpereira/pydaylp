class Presidente:

    instancia = None

    @staticmethod
    def getInstancia():

        if Presidente.instancia:
            return Presidente.instancia
        else:
            Presidente.instancia = Presidente()
            return Presidente.instancia


if __name__ == "__main__":

    pres1 = Presidente().getInstancia()
    pres2 = Presidente().getInstancia()
    pres3 = Presidente().getInstancia()

    print(pres1)
    print(pres2)
    print(pres3)


