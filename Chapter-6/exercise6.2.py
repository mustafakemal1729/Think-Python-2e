# Exercise 6-2.

"""

The Ackermann function, A(m, n) is defined:

    A(m, n): 
        n + 1 if m = 0
        A(m-1, 1) if m > 0 and n = 0
        A(m-1, A(m, n - 1)) if m > 0 and n > 0

Write a function named ack that evaluates the Ackermann function. 
Use your function to evaluate ack(3, 4), which should be 125. What happens for larger values of m and n?
"""

def ack(m, n):
    
    if m == 0:
        return n+1
    
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
    

print(ack(3, 4)) # -> 125
    
