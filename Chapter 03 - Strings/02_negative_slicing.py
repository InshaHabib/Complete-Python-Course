# Negative Slicing
name = "Insha Habib"
print(name[0:3])

print(name[-5:-1])

print(name[:5])  # [0:5]
print(name[6:])  # [4:length-1] is same as [6:11]
print(name[6:11])


# String with skip value
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[1:9:4]) # 1 se 9 ka andr 4,4 ka ghaib se btana ha

word = "amazing"
print(word[1:6:2])