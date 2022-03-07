# Exercise 4-3.

# I decided to look at Allen Downey's explanation for this question.

"""
Write an appropriately general set of functions that can draw shapes as in Figure 4-2.

"""

import math
import turtle


bob = turtle.Turtle() 

def draw_pie(t, n, r):
    # Draws a pie, then moves into position to the right.
    polypie(t, n, r)
    t.penup()
    t.forward(r*2 + 10)
    t.pendown()


def polypie(t, n, r):
    # Draws a pie divided into radial segments.
    angle = 360/ n
    for _ in range(n):
        isosceles(t, r, angle/ 2)
        t.left(angle)


def isosceles(t, r, angle):
    # Draws an icosceles triangle.

    y = r * math.sin(angle * math.pi / 180)

    t.right(angle)
    t.forward(r)
    t.left(90 + angle)
    t.forward(2 * y)
    t.left(90 + angle)
    t.forward(r)
    t.left(180 - angle)


bob.penup()
bob.backward(200)
bob.pendown()

# draw polypies with various number of sides
r = 80
draw_pie(bob, 5, r)
draw_pie(bob, 6, r)
draw_pie(bob, 7, r)

bob.hideturtle()
turtle.mainloop()