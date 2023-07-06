# 8. Write a Python script to merge two Python dictionaries.

# Used ** to merge two dictionaries
# Could use new_dict = dict1.copy() 
# then new_dict.update(dict2)
def merge_dict(dict1,dict2):
    new_dict = {**dict1,**dict2}
    return new_dict


dic1={1:10, 2:20}
dic2={3:30, 4:40}

print(merge_dict(dic1,dic2))