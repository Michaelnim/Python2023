# 14. Write a Python program to sort a given dictionary by key.

def sorted_dict(dict):
    for key in sorted(dict):
        print(key+":",  dict[key])


dict1 = {"red": 3, "green": 2, "blue": 1}

sorted_dict(dict1)