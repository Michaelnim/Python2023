# 3. Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Using ** operator to concatenate all dictionaries into one
def append_dict(dict1,dict2,dict3):
    new_dict = {**dict1,**dict2,**dict3}
    return new_dict


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

print(append_dict(dic1,dic2,dic3))