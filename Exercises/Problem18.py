# 18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

# Function to return total of nums
# If they are the same total*3
def sum(num1,num2,num3):
    total = num1 + num2 + num3
    return total*3 if num1 == num2 and num1 == num3 else total

# Variables to test
nums1 = 1
nums2 = 1
nums3 = 1

print(sum(nums1,nums2,nums3))