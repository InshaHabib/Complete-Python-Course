# Init_Constructor: Constructor is a special method which is automatically called when an object of a class is created. 
# It is used to initialize the attributes of the class.

class Employee:
    language = "Python"
    salary = 100000
    
    # _init_: dunder methid which is called automatically called when an object is created.
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
    
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod # :- staticmethod doesn't take self parameter.
    def greet():
        print("Good Morning")
    
jerry = Employee("Insha", 120000, "React")
# jerry.name = "Insha"
print(jerry.name, jerry.salary, jerry.language)
 
