# # Exercise 3-3.

"""
Note: This exercise should be done using only the statements and other features we
have learned so far.

1. Write a function that draws a grid like the following:

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

Hint: to print more than one value on a line, you can print a comma-separated sequence of values:
    print('+', '-')

By default, print advances to the next line, but you can override that behavior
and put a space at the end, like this:
    print('+', end=' ')
    print('-')

The output of these statements is '+ -'.
A print statement with no argument ends the current line and goes to the next line.

2. Write a function that draws a similar grid with four rows and four columns.

"""

# Solution for exercise 3.3.1

def draw_grid():
    draw_horizontal()
    draw_vertical()
    draw_horizontal()
    draw_vertical()
    draw_horizontal()

def draw_horizontal():
    print("+ - - - - + - - - - +")

def draw_vertical():
    print('|         |         |\n'*4, end='')


draw_grid()
print()


# Solution for exercise 3.3.2

def draw_four_by_four_grid():
    draw_new_horizontal()
    draw_new_vertical()
    draw_new_horizontal()
    draw_new_vertical()
    draw_new_horizontal()
    draw_new_vertical()
    draw_new_horizontal()
    draw_new_vertical()
    draw_new_horizontal()

def draw_new_horizontal():
    print('+ - - - - + - - - - + - - - - + - - - - +')

def draw_new_vertical():
    print('|         |         |         |         |\n'*4, end='')


draw_four_by_four_grid()