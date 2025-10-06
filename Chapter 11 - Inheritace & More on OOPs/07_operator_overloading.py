# Operator Overloading in Python

class number:  
    def __init__(self, n):
        self.n = n
        
    def __add__(self, num):
        return self.n + num.n

n = number(1)
m = number(2)

print(n + m) 

"""Operators that can be overloaded:
p1 + p1 # p1.__add__(p2)
p1 - p1 # p1.__sub__(p2)
p1 * p1 # p1.__mul__(p2)
p1 / p1 # p1.__truediv__(p2)
p1 // p1 # p1.__floordiv__(p2)
"""

# dunder/magic methods in python:-
# str__() #used to set what gets displayed upom calling str(obj)
# __len__() #used to set what gets displayed upon calling len(obj)
