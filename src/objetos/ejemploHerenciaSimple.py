class Animal:

    def __init__(self, name):
        self.__name = name

    def sayHello(self):
        print("Hello")


class Dog(Animal):

    def sayHello(self):
        print("Guau guau!!!")


class Cat(Animal):

    def __init__(self,name):
        print("Cat constructor")
        super(Cat, self).__init__(name)

    def sayHello(self):
        print("Miau miau!!!")


if __name__ == "__main__":

    doggy = Dog("Toby")
    michi = Cat("Vigotes")

    doggy.sayHello()
    michi.sayHello()

