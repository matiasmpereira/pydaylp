class Animal:

    __count = 0

    @staticmethod
    def __addOne():
        Animal.__count += 1

    @staticmethod
    def count():
        return Animal.__count

    def __init__(self, name):
        self.__name = name
        Animal.__addOne()

    def sayHello(self):
        print("Hi I'm {0}".format(self.__name))


if __name__ == "__main__":

    doggy = Animal("Doggy")
    michi = Animal("Michi")

    doggy.sayHello()
    michi.sayHello()

    print("Total: {0}".format(str(Animal.count())))

