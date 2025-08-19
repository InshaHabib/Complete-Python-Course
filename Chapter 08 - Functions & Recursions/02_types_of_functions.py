# Types of functions in Python
# 1. Built-in functions:- 
# built-in functions are functions that are already defined in Python.
# (defined by Python)

# 2. User-defined functions :-
# user defined functions are functions that are defined by the user to perform specific tasks.
# (defined by user... it's own logic)

# Functions with arguments:-

def func(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "OK" # function value given to any variable (return value)
    
a = func("Insha","Thank You") # name is parameter/argument
print(a) # None is returned as no return value is specified in the function
func("Jerry","Thank You") # name is parameter/argument
func("Sunflower","Thanks") # name is parameter/argument