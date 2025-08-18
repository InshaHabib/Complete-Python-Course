#  Program to calculate the factrorial of a given number using for loop.

# 6! = 6*5*4*3*2*1 = 720
num = int(input("Enter a number to find its factorial: "))

fac = 1
for i in range(1, num + 1):
    fac = fac * i
    
print(f"The factorial of {num} is {fac}")