# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

# Funtion to return new array of odd numbers
def odd_list(l1):
    # Iterating through l1 to find all odd numbers and adding them
    new_array = [x for x in l1 if x % 2 == 1]
    return new_array

# array of numbers
num_array = [1,2,3,4,5]

print(odd_list(num_array))