# ttProgram to rename a file to "renamed_by_python.txt".

with open("old.txt") as f:
    data = f.read()
    
with open("renamed_by_python.txt","w") as f:
    f.write(data)

