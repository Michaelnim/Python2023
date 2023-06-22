# 16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

# Function to compare if num > 17 or < 17
def diff(num):
    if num > 17:
        return abs(17-num)*2
    else:
        return 17 - num

# Variables to test
num1 = 17
num2 = 18

# Calling for function
print(diff(num1))
print(diff(num2))