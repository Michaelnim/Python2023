# 34. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

def two_sum(num1,num2):
    sum = num1 + num2
    if sum < 15 or sum > 20:
        return sum
    else:
        return 20

num1 = 5
num2 = 10

print(two_sum(num1,num2))