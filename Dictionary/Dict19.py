# 19. Write a Python program to combine two dictionary by adding values for common keys.

#Used counter from collections
from collections import Counter

# Function to add the values with same keys using Counter
def combine(dict,dict2):
    new_dict = Counter(dict) + Counter(dict2)
    return new_dict

dict1 = {"a":1,"b":2,"c":3}
dict2 = {"a":1,"b":2,"c":3,"d":10}

print(combine(dict1,dict2))