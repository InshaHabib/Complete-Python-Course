# File Functions
f = open("file.txt", "r")  # open file in read mode
'''lines = f.readlines()  # read all lines of the file
print(lines, type(lines))  # print the list of lines
# f.close()  # close the file'''

'''line1 = f.readline()  # read one line at a time
print(line1, type(line1))

line2 = f.readline()  # read one line at a time
print(line2, type(line2))

line3 = f.readline()  # read one line at a time
print(line3, type(line3))

line4 = f.readline()  # read one line at a time
print(line4, type(line4))

line5 = f.readline()  # read one line at a time
print(line5 == "")'''

line = f.readline()  # read one line at a time
while(line != ""):
    print(line)
    line = f.readline()  # read next line
f.close()