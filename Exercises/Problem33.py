# 33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

# Takin 3 numbers and giving its sum
# If any of the 3 numbers matches another return 0
def sum_of_three(num1,num2,num3):
    if num1 == num2 or num1 == num3 or num2 == num3:
        return 0
    else:
        return num1 + num2 + num3

nums1 = 1
nums2 = 2
nums4 = 3

print(sum_of_three(nums1,nums2,nums4))