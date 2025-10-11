# create a class employee and add salary and increment properties in it.
# write a method 'salaryafterincrement' method with a @property decorator 
# with a setter which changes the value of increment based on the salary.

class Employee:
    salary = 100000
    increment = 20
    
    @property # Return any value/function/variable
    def salaryAfterIncrement(self):
       return (self.salary + self.salary * (self.increment / 100))
    
    @salaryAfterIncrement.setter # changes the value of increment based on salary
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1)* 100
        
a = Employee()
print(a.salaryAfterIncrement)
a.salaryAfterIncrement = 120000
print(a.increment)


