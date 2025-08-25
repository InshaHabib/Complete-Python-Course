# The game() function in a program lets a user play a game and returns the score as an previous Hi-score. 
# You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. 
# You need write a program to update Hi-score whenever the game() fucntion breaks the Hi-score.

import random

def game():
    print("Welcome to the game!")
    print("You are playing the game...")
    score = random.randint(1, 62)
    
    # fetch the previous Hi-score
    with open('hiscore.txt', 'r') as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
        
    print(f"Your score is: {score}")
    if(score > hiscore or hiscore == ""):
    # write the new Hi-score to the file
        with open('hiscore.txt', 'w') as f:
            f.write(str(score))
   
    return score

game()