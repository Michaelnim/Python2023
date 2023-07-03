# 28. Write a Python program to find the second largest number in a list.

# Function to find 2nd biggest in list
def second_biggest(list):
    # If len(list) is < 2 return none
    if len(list) < 2:
        return None
    # Sorted list to print out the 2nd biggest
    new_list = sorted(list)
    return new_list[-2]

l1 = [1,2,3,4,5]

print(second_biggest(l1))