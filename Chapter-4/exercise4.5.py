# Exercise 4-5

"""
Read about spirals at http://en.wikipedia.org/wiki/Spiral; then write a program that draws an Archimedian spiral.
For more information: https://en.wikipedia.org/wiki/Archimedean_spiral
"""


# I decided to look at Allen Downey's explanation for this question.


import turtle
import math


def draw_spiral(t, n, length=3, a=0.05, b=0.0002):
    """
    Draws an Archimedian spiral starting at the origin.
    
    n: how many line segments to draw
    length: how long each segment is
    a: how loose the initial spiral starts out (larger is looser)
    b: how loosly coiled the spiral is (larger is looser)
    """
  
    theta = 0.0

    for _ in range(n):
        t.forward(length)
        dtheta = 1 / (a + b * theta)

        t.left(dtheta)
        theta += dtheta


# create the world and bob
bob = turtle.Turtle()
draw_spiral(bob, n=270)



bob.hideturtle()
turtle.mainloop()