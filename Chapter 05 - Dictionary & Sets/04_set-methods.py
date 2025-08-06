#  Set Methods 

s = {1, 32, 50, 5, 5, 5, 50, "Insha"}
print(s, type(s)) 

s.add(576)
print(s, type(s))

# len of set is start as 1 not 0
print(len(s))

s.remove(50)
print(s)

s.update({3,4,5})
print(s)

s.clear()
print(s)