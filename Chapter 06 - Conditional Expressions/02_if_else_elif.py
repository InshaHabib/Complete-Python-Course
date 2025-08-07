# Conditions: Is/else, elif

a = int(input("Enter your age= "))

if(a>=18):
    # space means indentation in python. 
    print("The person is young ")
    print("You are above the age of consent")
    
elif(a<0):
    print("You are entering an invalid -ve age")
    
elif(a==0):
    print("You ar entering 0 which is not valid age")
    
else:
    print("You are below the age of consent")

print("End of Program")