# 20. Write a Python program to access the index of a list.

# getting the index of elements
def index(l1):
    # enumerate takes list and gives them a index number/count
    new_list = [x for x in enumerate(l1)]
    return new_list
    
# Testing variables
testing = ["red","blue","yellow","green"]

print(index(testing))