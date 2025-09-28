# We all have played snake, water, gun game in our childhood. 
# If you haven't, google the rules of this game and 
# write a python program capable of playing this game with the user.

''' 
1 for snake
-1 for water 
0 for gun
'''
import random

computer = random.choice([1, 0, -1])  # 1 for snake, -1 for water, 0 for gun
user = input("Enter your choice: ")
dict = {"snake": 1, "water": -1, "gun": 0}
reversedict = {1: "snake", -1: "water", 0: "gun"}
you = dict[user]

# By now we have 2 numbers (variables), you and computer,

print(f"You choose {reversedict[you]}\nComputer chose: {reversedict[computer]}")

if(computer == you):
    print("It's a draw")
    
else:
    # 2nd method
    # This logic is written on the basis of the value of (computer - you)
    if(computer - you) == -1 or (computer - you) == 2:
        print("You lose")
    else:
        print("You win")