# Inheritance in Python: way of creating a new class from an existing class.

class employee: # base/parent class
    company = "UEP"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
        
# class programmer:
#     company = "UEP Karachi"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
        
#     def showlanguage(self):
#         print("The name is {self.name} and he is good with {self.language} language")
        
class programmer(employee): # inherited/derived/child class
    company = "UEP Karachi"
        
    def showlanguage(self):
        print("The name is {self.name} and he is good with {self.language} language")

a = employee()
b = programmer()

print(a.company, b.company)