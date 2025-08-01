#  Program to fill in a letter template given with name and date.

letter = ''' Dear <|Name|>,
            You are selected
            on <|Date|>'''

print(letter.replace("<|Name|>", "Insha Habib").replace("<|Date|>","1 August, 2025"))