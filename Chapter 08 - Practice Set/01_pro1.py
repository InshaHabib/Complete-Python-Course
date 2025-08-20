#  Program using functions to find greatest of three numbers.

# 1st method:-
def function():
    num1 =int(input("Enter the number1 = "))
    num2 =int(input("Enter the number2 = "))
    num3 =int(input("Enter the number3 = "))
    
    if num1>num2 and num1>num3:
        print(f"The greatest of three numbers is {num1}")
    
    elif num2>num1 and num2>num3:
        print(f"The greatest of three numbers is {num2}")
    
    # elif num3>num1 and num3>num2:
    else:
        print(f"The greatest of three numbers is {num3}")
        
function()
# The function will prompt the user to input three numbers and determine the greatest among them.

# ......................................................................
# 2nd method:-

def greatest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
a = int(input("Enter the number1 = "))
b = int(input("Enter the number2 = "))  
c = int(input("Enter the number3 = "))

print(f"The greatest of three numbers is {greatest(a, b, c)}")