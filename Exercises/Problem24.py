# 24. Write a Python program to test whether a passed letter is a vowel or not.

# Function to return true if it contains vowel else False
def is_vowel(char):
    return True if any(x in 'aeiouAEIOU' for x in char) else False

# Test variables
char = "a"
char2 = "b"
char3 = "c"

print(is_vowel(char))
print(is_vowel(char2))
print(is_vowel(char3))