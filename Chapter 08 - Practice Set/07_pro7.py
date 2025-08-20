# Python function to remove given word in a list and strip it at the same time.

def rem(list,word):
    n=[]
    for item in list:
        if isinstance(item, str):         # only apply to strings
            n.append(item.replace(word, ""))  # remove all occurrences of word
        else:
            n.append(item) 
    return n  
        
list = ["insha","jerry",20,"sunflower"]
print(rem(list,"er"))


# ............................................................................

'''def remove_word_and_strip(lst, word):
    return [item.replace(word, "").strip() 
            if isinstance(item, str)
            else item 
            for item in lst]  
# Python function to remove a given word from strings in a list and strip whitespace.   
# Example usage:
lst = ["  insha  ", "jerry", 20, "sunflower"]
print(remove_word_and_strip(lst, "er"))
'''


