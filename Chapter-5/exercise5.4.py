# Exercise 5-4.

"""
What is the output of the following program? 
Draw a stack diagram that shows the state of the program when it prints the result.

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
    recurse(3, 0)

1. What would happen if you called this function like this: recurse(-1, 0)?

2. Write a docstring that explains everything someone would need to know in order to use this function (and nothing else)

"""

# Solution for exercise 5.3.1

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
    
    recurse(3, 0)

# Recursive function to print the value of s while n is decreasing

"""
Answer:

    '__main__'

    recurse:
        n -> 3
        s -> 0
    
    recurse:
        n -> 2
        s -> 3
    
    recurse:
        n -> 1
        s -> 5
    
    recurse:
        n -> 0
        s -> 6

"""



# Solution for exercise 5.3.2

"""
Answer:
    recurse(-1, 0) will get RecursionError, because recurse(-1, 0) is infinite recursion

"""
