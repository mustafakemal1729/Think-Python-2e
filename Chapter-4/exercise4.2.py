# Exercise 4-2

# I decided to look at Allen Downey's explanation for this question.

"""
Write an appropriately general set of functions that can draw flowers as in Figure 4-1.

"""
import turtle
import math

bob = turtle.Turtle()

def square(t):
    for _ in range(4):
        t.forward(100)
        t.left(90)


def polygon(t, n, length):
    angle = 360 / n
    for _ in range(n):
        t.forward(length)
        t.left(angle)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference/10) +1
    length = circumference / n
    polygon(t, n, length)


def polyline(t, n, length, angle):
    for _ in range(n):
        t.forward(length)
        t.left(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 9) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    arc(t, r, 360)


def petal(t, r, angle):
    # Draws a petal using two arc

    for _ in range(2):
        arc(t, r, angle)
        t.left(180 - angle)

def flower(t, n, r, angle):
    # Draws a flower witn n petals

    for _ in range(n):
        petal(t, r, angle)
        t.left(360 / n)
    

def move(t, length):
    # move turtle forward without leaving a trail
    t.pu()
    t.fd(length)
    t.pd()

move(bob, -200)
flower(bob, 7, 60, 60)

move(bob, 200)
flower(bob, 10, 60, 90)

move(bob, 200)
flower(bob, 20, 130, 20)


bob.hideturtle()
turtle.mainloop()