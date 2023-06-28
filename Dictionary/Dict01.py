# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

# Function to print dictionary ascend/descend 
# used items to keep keys and values 
# used the value as a way to organize dict
def ascend_descend(dict):
    ascend = sorted(dict.items(), key=lambda x:x[1])
    descend = sorted(dict.items(), key=lambda x:x[1], reverse=True)
    return f"List ascending: {ascend} \nList descending: {descend}"
    


# Testing variable
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(ascend_descend(d))