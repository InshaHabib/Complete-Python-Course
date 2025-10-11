# create a class (2-D vector) and use it to create another class representing 3-D vector.

class TwoDVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print(f"The vector is {self.x}x + {self.y}y")
        
class ThreeDVector(TwoDVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        
    def show(self):
        print(f"The vector is {self.x}x + {self.y}y + {self.z}z  ")
 
a = TwoDVector(2, 4)
a.show()
b = ThreeDVector(2, 4, 6)
b.show()