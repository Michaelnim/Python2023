# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

# List of colors
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Variable to iterate through the list and turning them into tuples
# Using the index of the tuple to keep out 0th, 4th, and 5th element
sample_list = [x for (i,x) in enumerate(sample_list) if i not in (0,4,5)]

# Printing out new list
print(sample_list)