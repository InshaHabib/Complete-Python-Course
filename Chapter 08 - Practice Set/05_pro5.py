'''A python function to print 1st n lines of the following patterns.
***
**
**
for n=3
'''

def pattern(n):
    if n==0:
        return
    print("*" * n) 
    pattern(n-1)
    
pattern(int(input("Enter the number of rows for the star pattern: ")))