# create a class pet from a class animals and further create a dog class from pets. Add a method bar to class dog.

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("WOOF WOOF")
        
a = Dog()
a.bark()
