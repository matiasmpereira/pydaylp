from functools import reduce


class Persona:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def nombre(self):
        return self.__nombre

    def edad(self):
        return self.__edad

    def __repr__(self):
        return "{0}->{1}".format(self.__nombre,self.__edad)


if __name__ == "__main__":

    personas = [Persona("Juan", 17), Persona("Maria", 37), Persona("Carlos", 56)]
    print(list(map(lambda persona: "Hola {0}".format(persona.nombre()), personas)))
    print(list(filter(lambda persona: persona.edad() >= 18, personas)))
    mulEdades = reduce(lambda acum, edad: acum*edad, map(lambda per: per.edad(), personas))
    print("Total multiplicacion edades: {0}".format(mulEdades))





