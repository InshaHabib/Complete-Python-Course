# Self Parameter:-

class Employee:
    # Class Attributes:-
    # name = "insha"
    language = "Python"
    salary = 100000
    
    # function:-
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod # :- staticmethod doesn't take self parameter.
    def greet():
        print("Good Morning")
    
jerry = Employee()
jerry.name = "Jerry"
jerry.language = "React" # Object/instance Attribute:- take preference over class attributes during assignment & retrieval.
# print(jerry.name,jerry.language, jerry.salary)

jerry.greet()
jerry.getinfo()
# Employee.getinfo(jerry) # same as jerry.getinfo() - here jerry is passed as self parameter.
