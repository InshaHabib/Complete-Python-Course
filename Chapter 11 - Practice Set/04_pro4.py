# Write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*' which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
        
    def __add__(self, c1):
        return Complex(self.r + c1.r, self.i + c1.i)
    
    def __mul__(self, c1):
        real_part = self.r * c1.r - self.i * c1.i
        imag_part = self.r * c1.i + self.i * c1.r
        return Complex(real_part, imag_part)
            
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
c = Complex(1, 2)
c1 = Complex(3, 4)
print("Sum:", c + c1)
print("Multiplication:", c * c1)


"""class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
        
    def __add__(self, c1):
        return Complex(self.r + c1.r, self.i + c1.i)
    
    def __mul__(self, c1):
        return Complex(self.r * c1.r, self.i * c1.i)
    
a = Complex(4,8)
b = Complex(2,6)
c = a.__add__(b)
d = a.__mul__(b)
print(f"Sum: {c.r} + {c.i}i")
print(f"Multiplication: {d.r} + {d.i}i")"""