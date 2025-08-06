# Create an empty dictionary. Allow 4 friends to enter their favourite language as value 
# and use key as their names. Assume that the names are unique.

dict = {}

n1 = input("Enter your name= ")
f1 = input("Enter your favo urite language= ")
dict.update({n1 : f1})

n2 = input("Enter your name= ")
f2 = input("Enter your favourite language= ")
dict.update({n2 : f2})

n3 = input("Enter your name= ")
f3 = input("Enter your favourite language= ")
dict.update({n3 : f3})

n4 = input("Enter your name= ")
f4 = input("Enter your favourite language= ")
dict.update({n4 : f4})

print(dict)

