# File I/O - Input/Output operations

# RAM - Random Access Memory = Volatile memory :- All program and data is stored in RAM while the computer is on.
# HDD - Non - Volatile memory :- All program and data is stored in HDD
# For percist data we use HDD

# A file i s data stored in device. A python program can talk to the file by reading content from it and writing content (data) to a file.

f = open("file.txt", "r")  # open file in read mode
data = f.read()  # read content of file
print(data)
f.close()  # close the file

'''Types of files:-
1. Text files - .txt, .csv, .html, .xml
2. Binary files - .jpg, .png, .mp3, .mp4, .pdf, .docx'''

