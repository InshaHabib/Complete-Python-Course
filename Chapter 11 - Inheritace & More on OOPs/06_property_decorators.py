# Property Decorators in Python :- are used to define methods in a class which can be accessed like attributes.
# They are used to add getter, setter and deleter functions in a class.

# Class Method in Python
class employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")
        
    @property
    def name(self):
        return  f"{self.fname}{self.lname}"
    
    @name.setter
    def name (self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        
e = employee()
e.a = 45

e.name = "Insha Habib"
print(e.fname,e.lname)

e.show()






