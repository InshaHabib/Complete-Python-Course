# Create a class "Programmer" for strong info of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
        
p = Programmer ("Insha", 100000, 411057)
print(p.name, p.salary, p.pincode, p.company)
 
p = Programmer ("Jerry", 120000, 41127)
print(p.name, p.salary, p.pincode, p.company)    
    
p = Programmer ("Sunflower", 80000, 41257)
print(p.name, p.salary, p.pincode, p.company)
    
