# Program to find out whether a file is identical & matches the content of another file.

with open("this.txt") as f:
    data1 = f.read()
    
with open("this_copy.txt","r") as f:
    data2 = f.read()

if(data1 == data2):
    print("Yes these are identical and match")
    
else:
    print("No these are not identical and match")