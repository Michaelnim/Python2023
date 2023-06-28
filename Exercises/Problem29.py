# 29. Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

# Finding the difference from l1 and l2
# returning l3 with the difference
def difference(l1,l2):
    l3 = set(l1) - set(l2)
    return l3



color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(difference(color_list_1,color_list_2))
