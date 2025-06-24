class Animal :
    def _init_(self) :
        print("Animal Created")
class Dog(Animal) :
    pass
d= Dog()
d._init_()