# Property Decorators in Python

# Class Method in Python
class employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")
        
    @property
    def name(self):
        return self.ename
    
    @name.setter
    def name (self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        
e = employee()
e.a = 45

e.name = "Insha Habib"
print(e.name)

e.show()




# 

