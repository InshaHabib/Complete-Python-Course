# Write a python program to print the content of directory using the os module.
# Search online for the function which does that
# Label the program written with comments

import os

# specify the path you want to check
path = "D:/Python New Course"

# get the list of files and directories
content = os.listdir(path)

print("Contents of directory:", path)
for item in content:
    print(item)
