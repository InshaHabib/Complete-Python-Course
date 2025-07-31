#  String Functions

name = "Insha Habib"
print(len(name))
print(name.endswith("bib"))
print(name.startswith("ins"))  # False bcz of small letter
print(name.startswith("Ins"))  # True

nickname = "jerry"
print(nickname.capitalize()) # capital only 1st character

print(nickname.lower())  
print(name.upper())  

index = name.find("bib")
print(index)

s = "HTML CSS JS"
replaced = s.replace("JS","Python")
print(replaced)


# Removes whitespace (or characters) from both ends.

"  hello  ".strip()    #  "hello"
"  hello".lstrip()     #  "hello"
"hello  ".rstrip()     #  "hello"


# Check types of characters

"abc".isalpha()   #  True
"123".isdigit()   #  True
"abc123".isalnum() #  True