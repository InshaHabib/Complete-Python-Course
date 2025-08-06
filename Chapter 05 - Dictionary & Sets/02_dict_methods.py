# Dictionary Methods

d = {} # --- Empty Dictionary

marks = {
  "insha": 90,
  "jerry": 85,
  "sunflower": 95, 
  "list" : [1,2,3,4,5,8]
 }

print(marks.items()) # all dictionary
print(marks.keys()) # only keys like insha....
print(marks.values()) # only values like 90....

marks.update({"insha": 95})
print(marks)

print(marks.get("jerry"))

# # print(marks.get("jerry2")) # print none
# # print(marks["jerry2"])  # Error

print(marks.copy()) # copy of dictionary

print(marks.pop("sunflower"))
