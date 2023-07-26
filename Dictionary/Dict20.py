# 20. Write a Python program to print all distinct values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Function to return unique values
def unique_value(dict):
    # set returns only one of the same value
    # iterating through dict then x to find values
    new_dict = set(x for x in dict for x in x.values())
    return new_dict

dict1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
new_dict = {}

print(unique_value(dict1))
