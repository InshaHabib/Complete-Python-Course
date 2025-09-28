# OOP - focuses on using reusable code (DRY Principle) - means Do not repeat yourself.

# Class:- A class is a blueprint for creating object.
# Object:- An object is an instance of a class. When the class is defined, a new namespace is created, and used as the local scope for all its methods.

""" Noun = class = Employee
Adjective =  Attributes = name, language, salary
Verb = Methods = getsalry(), increment() """

class Employee:
    # Class Attributes:-
    # name = "insha"
    language = "Python"
    salary = 100000
    
insha = Employee()
insha.name = "Insha" # Object/instance Attribute
print(insha.name,insha.language, insha.salary)
    
jerry = Employee()
jerry.name = "Jerry"
print(jerry.name,jerry.language, jerry.salary)
    
"""Here, name is object/instance attribute & salary and language are class attributes 
as they directly belong to the class."""

