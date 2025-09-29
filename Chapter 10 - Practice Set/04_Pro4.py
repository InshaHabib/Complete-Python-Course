# Add a static method in problem 2, to greet the user with hello.

class calculator:
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"The square is {self.n*self.n}")
        
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
        
    def square_root(self):
        print(f"The aquare is {self.n**1/2}")
        
    @staticmethod
    def hello():
        print("Hello user, wellcome to the program")

a = calculator(int(input("Enter a number = ")))

a.hello()

a.square()
a.cube()
a.square_root()
    