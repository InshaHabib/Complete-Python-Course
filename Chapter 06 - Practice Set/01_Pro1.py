# Program to find the greatest of 4 numbers entered by the user.
num1 = int(input("Enter the number1 = "))
num2 = int(input("Enter the number2 = "))
num3 = int(input("Enter the number3 = "))
num4 = int(input("Enter the number4 = "))

if(num1>num2 and num1>num3 and num1>num4):
    print("Number1 is the greatest of 4 numbers")
    
elif(num2>num1 and num2>num3 and num2>num4):
    print("Number2 is the greatest of 4 numbers")
    
elif(num3>num1 and num3>num2 and num3>num4):
    print("Number3 is the greatest of 4 numbers")
    
else:
    print("Number4 is the greatest of 4 numbers")
    
