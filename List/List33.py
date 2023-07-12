# 33. Write a Python program to generate all sublists of a list.

# Creating sublist of a list
def sublists(list):
    # Variable to hold new list containing all sub list
    new_list = [[]]
    # Iterating through the length of the list
    for i in range(len(list)+1):
        # Iterating depending on i
        for j in range(i):
            new_list.append(list[j:i])
    return new_list


list = ["a","b","c"]

print(sublists(list))
