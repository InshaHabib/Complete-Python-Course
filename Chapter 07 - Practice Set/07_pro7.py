'''Program to print the following star patterns
for n=3
  *
 ***
***** 

for n=5
    *
   ***
  ***** 
 ******** 
**********
'''

num = int(input("Enter the number of rows for the star pattern: "))

for i in range (1,num+1):
    print(" "* (num-i), end="")
    print("*"* (2*i-1), end="")
    print("") # for new line
    
    