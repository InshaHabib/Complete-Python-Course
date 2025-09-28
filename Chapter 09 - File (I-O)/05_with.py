# With Statement:- The best way is to open and close a file using with statement.

f = open("file.txt", "r")
data = f.read()
print(data)
f.close()

# The same code using with statement like this:-
with open("file.txt", "r") as f:
    data = f.read()
    print(data) 