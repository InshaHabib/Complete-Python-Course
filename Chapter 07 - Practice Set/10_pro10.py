# Program to print the multiplication table of n using for loops in reversed order.

num = int(input("Enter any number to print its multiplication table: "))


for i in range(1,13):
    print(f"{num} * {13-i} = {num*(13-i)}")
    
    