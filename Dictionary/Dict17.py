# 17. Write a Python program to remove duplicates from the dictionary.

# Phone contacts of people (dictionary)
phone_number = {'key1':
                {"name": ["Random"],
                 "phone": [111-1111],
                 "carrier": ["T-mobile"]
                 },
                "key2":
                {"name": ["RnG"],
                 "phone": [222-2222],
                 "carrier": ["Verizon"]
                },
                "key3":
                {"name": ["Ran2"],
                 "phone": [222-2222],
                 "carrier": ["Verizon"]
                },
                "key4":
                {"name": ["Random"],
                 "phone": [111-1111],
                 "carrier": ["T-mobile"]
                 },
                }

# Creating new dictionary to hold new data
new_dict = {}

#Iterating through phone number{}
for key, value in phone_number.items():
    # If value is not in new_dict then add it
    if value not in new_dict.values():
        new_dict[key] = value
# Printing new dictionary without duplicates
print(new_dict)