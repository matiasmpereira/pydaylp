class TableroBingo:

    def __init__(self):
        self.__participantes = []

    def agregarParticipante(self, participante):
        self.__participantes.append(participante)


    def eliminarParticipante(self, participante):
        self.__participantes.remove(participante)


    def informarNumero(self, numero):
        for participante in self.__participantes:
            participante.nuevoNumero(numero)


class Participante:

    hayGanador = False

    def __init__(self, carton):
        self.__carton = carton
        self.__aciertos = 0

    def nuevoNumero(self,numero):

        if self.__aciertos == len(self.__carton):
            print("Bingo, mi juego favorito")
            Participante.hayGanador = True
        else:
            if numero in self.__carton:
                # Lo tacho
                self.__aciertos += 1


if __name__ == "__main__":

    tablero = TableroBingo()
    p1 = Participante([4,  11, 99, 3,  8,  29])
    p2 = Participante([98, 10, 40, 33, 28, 29])
    p3 = Participante([5,   2,  0,  4,  1,  3])

    tablero.agregarParticipante(p1)
    tablero.agregarParticipante(p2)
    tablero.agregarParticipante(p3)

    i = 0
    while not Participante.hayGanador and i < 100:
        tablero.informarNumero(i)
        print(str(i))
        i += 1

    tablero.eliminarParticipante(p1)
    tablero.eliminarParticipante(p2)
    tablero.eliminarParticipante(p3)



