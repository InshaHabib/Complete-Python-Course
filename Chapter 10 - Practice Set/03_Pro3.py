# Create a class with a class attribute a: create an object from it and set 'a' directly using object.a = 0. 
# Does This change the class attribute? ////// Answer:- No 

class Programmer:
    a = 4 # class attribute

o = Programmer()
print(o.a) # prints class attribute because instance attribute is not present.

o.a = 0 # instance attribute is created 

print(o.a) # print instance attribute because instance attribute is present.

print(Programmer.a) # prints the class attribute
