# We all have played snake, water gun game in our childhood. 
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
    # 1st method
    if(computer == -1 and you ==  1): # (computer -you) -2
        print("You win")
        
    elif(computer == -1 and you == 0): # -1
        print("You lose")
        
    elif(computer == 1 and you == -1): # 0
        print("You lose")
        
    elif(computer == 1 and you == 0): # 1
        print("You win")
        
    elif(computer == 0 and you == -1): # 1
        print("You win")
        
    elif(computer == 0 and you == 1): # -1
        print("You lose")
         
    else:
        print("Something went wrong! Please try again.")
        