# Exercise 7-3.

"""

Write a function called estimate_pi that uses this formula to compute and return an estimate of π. 
It should use a while loop to compute terms of the summation until the last term is smaller than 1e-15.
You can check the result by comparing it to math.pi
"""

import math

def factorial(n):
    memo = {}
    if n in memo:
        return memo[n]

    elif n <= 1:
        return 1

    else:
        x = n * factorial(n-1)
        memo[n] = x
        return x
        

def estimate_pi():

    k = 0
    induction = 0
    last_term = 1
    while last_term > 1e-15:

        last_term = ((factorial(4 * k)) * (1103 + 26390 * (k))) / \
            ((factorial(k) ** 4) * (396 ** (4 * k)))
        k += 1.0
        induction += last_term

    result = ((2 * math.sqrt(2)) / 9801) * induction
    return 1/result


print(estimate_pi())
print(math.pi)


