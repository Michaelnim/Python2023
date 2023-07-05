# 2. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# Function to add key
def add_key(dict):
    # Checking dict if it has key = "2"
    if "2" not in dict:
        # If not then add it
        dict["2"] = 30
    return dict


dict1 =  {0: 10, 1: 20}

print(add_key(dict1))