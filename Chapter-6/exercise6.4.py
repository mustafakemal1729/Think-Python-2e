# Exercise 6-4.

"""

A number, a, is a power of b if it is divisible by b and a/b is a power of b. 
Write a function called is_power that takes parameters a and b and returns True if a is a power of b. 
Note: you will have to think about the base case.
"""


def is_power(a, b):

    if a == 1:
        return True
    elif b == 0 or a % b != 0 or a < b:
        return False
    else:
        return is_power(a/b, b)
