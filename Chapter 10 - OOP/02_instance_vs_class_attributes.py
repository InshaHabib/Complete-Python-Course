
class Employee:
    # Class Attributes:-
    # name = "insha"
    language = "Python"
    salary = 100000
    
jerry = Employee()
jerry.name = "Jerry"
jerry.language = "React" # Object/instance Attribute:- take preference over class attributes during assignment & retrieval.
print(jerry.name,jerry.language, jerry.salary)