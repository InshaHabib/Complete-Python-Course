# Append mode means :- we add more content to the existing file content.

st = "Hey Insha Habib, welcome to the world of Python programming.\n"

f = open("myfile.txt", "a")  # open file in write mode    
f.write(st)  # write content to file
f.close()  # close the file

 
# + - open for updating (reading and writing)
# 'rb'- open for reading in binary format
# 'rt' - open for reading in text format (default)