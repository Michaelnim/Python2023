# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

# Function that has 2 arguments
# N = the length of the word
# str = string of words
def longer_word(n , str):
    # Empty list to add new words into
    new_list = []
    # .split to seperate the words into there index
    txt = str.split(" ")
    # For loop to iterate through the list of splited words
    for i in txt:
        # Condition if the lenth of the word is > N append to new list
        if len(i) > n:
            new_list.append(i)
    return new_list

print(longer_word(3, "A list of words that are greater than 3"))