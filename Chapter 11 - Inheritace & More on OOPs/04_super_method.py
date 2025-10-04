# Super Method():-

class employee: # base/parent class
    def __init__(self): # constructor 
        print("Constructor of Emplpoyee class")
    a = 1

class programmer(employee):
    def __init__(self):
        print("Constructor of programmer class")
    b = 2
    
class manager(programmer):
    def __init__(self):
        super().__init__() # for access of parent class constructor 
        print("Constructor of manager class")
    c = 3
   
   
# o = employee()
# print(o.a) # print the a attribute   

# print(o.b) # error

# o = programmer()
# print(o.a, o.b) # print the a and b attribute

o = manager()
print(o.a, o.b, o.c) # print the a, b and c attribute


