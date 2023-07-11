# 15. Write a Python program to get the maximum and minimum values of a dictionary.

# created two variables to hold the min and max
def min_max(dict):
    min_value = min(dict.values())
    max_value = max(dict.values())
    return f"Max value: {max_value} \nMin value: {min_value}"


dict1 = {"a": 5, "b": 10, "c":1}

print(min_max(dict1))
