#  Program to find out whether a given post is talking about "Insha Habib" or not.


# post = "Hey Insha habib is sensitive. Insha habib is a graduate software engineer from FURC. Insha habib goal is to grow as a pythhon developer."

post = input("Enter your post = ")

if("Insha".lower() in post.lower()):
    print("This post is talking about about insha.")

else:
    print("There was no mention of insha in this post.")