# Multiple Inheritance

class employee: # base/parent class
    company = "UEP"
    name = "Insha Habib"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
        
class coder:
    language = "PYTHON"
    def printlanguage(self):
        print(f"Out of all the languages, here is her language: {self.language} ")
        
class programmer(employee, coder): # inherited/derived/child class
    company = "UEP Karachi"        
    def showlanguage(self):
        print(f"The company name is {self.company} and she is good in {self.language} language")

a = employee()
b = programmer()

b.show()
b.printlanguage()
b.showlanguage()