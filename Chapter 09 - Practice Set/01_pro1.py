# Program to read the text from a given file 'poem.txt' and find out whether it containes the word 'twinkle'.


f = open('poem.txt', 'r')
data = f.read()

if 'twinkle' in data:
    print("Yes, the word 'twinkle' is present in the file.")
else:
    print("No, the word 'twinkle' is not present in the file.")
    
f.close()

