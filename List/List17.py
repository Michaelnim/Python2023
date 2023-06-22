# 17. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False

# Finding prime number
def prime(l1):
    # Iterating through list
    for i in l1:
        # 0 can never be a prime -> False
        if i == 0:
            return False
        # 1 can never be prime -> False
        if i == 1:
            return False
        # 2 is prime -> True
        if i == 2:
            return True
        else:
            # checking if any number above 2 is prime
            # i.e (2,3)
            for x in range(2,i):
                # 3 % 2 != 0 -> True (prime)
                # 4 % 2 == 0 -> False (not prime)
                if(i%x==0):
                    return False
            return True



test = [4]

print(prime(test))