
a = int(input("Enter your age= "))

#  If statement 01
if(a%2 == 0):
    print("Age is even")
#   End of If statement 01

#  If statement 02
if(a>=18):
    # space means indentation in python. 
    print("The person is young ")
    print("You are above the age of consent")
    
elif(a<0):
    print("You are entering an invalid -ve age")
    
else:
    print("You are below the age of consent")
#   End of If statement 02

# print("End of Program")