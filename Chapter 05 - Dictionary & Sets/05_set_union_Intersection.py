# Union , Intersection in set

s1 = {1, 45, 2, 67}
s2 = {7, 8, 1, 2, 78}

print(s1.union(s2))

print(s1.intersection(s2))

# print(s1-s2) # Difference

print({1,2}.issubset(s1))
print(s1.issuperset({1,2}))