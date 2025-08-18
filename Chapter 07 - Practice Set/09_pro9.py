''' Program to print the following star patterns
for n=3
* * *
*   *
* * *
'''


num = int(input("Enter the number for the star pattern: "))

for i in range(1, num+1):
    if i == 1 or i == num:
        print("*" * num, end="")

    else:
        print("*", end="")
        print(" "*(num-2), end="")
        print("*", end="")
    print("")  # for new line