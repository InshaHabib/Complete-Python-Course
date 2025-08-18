# write a program to print table of a given numbers using for loop.

num = int(input("Enter a number to print its multiplication table: "))

for i in range(1, 13):
    print(f"{num} * {i} = {num * i}")
# Output will be the multiplication table of the given number from 1 to 10.
