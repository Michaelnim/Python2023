# 21. Write a Python program to convert a list of characters into a string.

# Function to join char list into a string
def string(str):
    return "".join(x for x in str)

# List of char
character = ["h","e","l","l","o"]

# Calling for function
print(string(character))

