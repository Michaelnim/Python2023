# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

#Function to check if len of word/num is > 2
#Using index 0 and -1 to see if first and last char match
def matching_char(list):
    match = 0
    #For loop to check if word/num > 2
    for i in list:
        if len(i) >= 2 and i[0] == i[-1]:
            match +=1
    return match

#List of words/num
sample_list = ['abc', 'xyz', 'aba', '1221']

#calling function
print(matching_char(sample_list))