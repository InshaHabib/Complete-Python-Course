#  Program to find the sum of first n natural numbers using while loop.

num = int(input("Enter a number to find the sum of first n natural numbers: "))

i=1
sum=0
while(i<=num):
    sum = sum + i
    i = i + 1
    
print(f"The sum of first {num} natural numbers is: {sum}")
# Output will be the sum of first n natural numbers.    
