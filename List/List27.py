# 27. Write a Python program to find the second smallest number in a list.

# Function to find the 2nd smallest number in list
def second_smallest(list):
    # If list is smaller than 2 return None
    if len(list) < 2:
        return None
    # Sorted list then returns 2nd element
    new_list = sorted(list)
    return new_list[1]


l1 = [1,-1,0,3,4]

print(second_smallest(l1))