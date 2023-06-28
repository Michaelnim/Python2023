# 21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

# Function to return "Even" if num % 2 == 0 else "Odd"
def even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print(even_odd(2))
print(even_odd(3))