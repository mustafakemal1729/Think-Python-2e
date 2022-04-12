# Exercise 6-1.

"""

Draw a stack diagram for the following program. What does the program print?

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))
"""


"""
Answer:

    '__main__'

    Global frame:
    
        b -> b(z)

        a -> a(x, y)

        c -> c(x, y, z)
                x	1
                y	5
                z	3
                total 9
        
        b -> b(9)

        a -> a(9, 9)
                x	10
                y	9
                Return value 90
        
        b -> b(9)
            z 9
            prod 90
            Return value 90


        c ->
            x	1
            y	5
            z	3
            total	9
            square	8100
            Return value 8100

9 90
8100
"""