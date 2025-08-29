# Program to make a copy of text file "this.txt".

with open("this.txt", "r") as f:
    data = f.read()
    
with open("this_copy.txt","w") as f:
    f.write(data)
    