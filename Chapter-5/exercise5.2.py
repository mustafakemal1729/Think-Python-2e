# Exercise 5-2.

"""

Fermat's Last Theorem says that there are no positive integers a, b, and c such that
a^n + b^n = c^n for any values of n greater than 2.

1. Write a function named check_fermat that takes four parameters — a, b, c and n and checks to see if Fermat's theorem holds. 
If n is greater than 2 and a^n + b^n = c^n the program should print, “Holy smokes, Fermat was wrong!” 
Otherwise the program should print, “No, that doesn't work.”

2. Write a function that prompts the user to input values for a, b, c and n, converts
them to integers, and uses check_fermat to check whether they violate Fermat's theorem.
"""

# Solution for exercise 5.2.1

def check_fermat(a, b, c, n):
    if n <= 2:
        print("n must be greater than 2")
    elif (a**n + b**n) == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


# Solution for exercise 5.2.2

def get_values_and_check_fermat():
    
    a = int(input('Enter a value for a: '))
    b = int(input('Enter a value for b: '))
    c = int(input('Enter a value for c: '))
    n = int(input('Enter a value for n: '))

    return check_fermat(a, b, c, n)