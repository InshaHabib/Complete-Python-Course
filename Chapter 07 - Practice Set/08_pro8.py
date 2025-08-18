'''Program to print the following star patterns
for n=3
*
**
***
'''

num = int(input("Enter the number of rows for the star pattern: "))

for i in range(1, num+1):
    print("*" * i, end="")
    print("")  # for new line
