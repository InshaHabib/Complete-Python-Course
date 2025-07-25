# Install an external module and use it to perform an operation of your interest
# pip install pyttsx3 - run by text to speak

import pyttsx3
engine = pyttsx3.init()

engine.say('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night. ''')

engine.runAndWait()


# import numpy as np

# numbers = [4, 9, 16, 25]
# sqrt_numbers = np.sqrt(numbers)
# print("Square roots:", sqrt_numbers)