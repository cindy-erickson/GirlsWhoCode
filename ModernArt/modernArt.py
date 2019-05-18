import turtle
from random import *

shape("turtle")

# color(150, 0, 150)
# red = randint(0, 255)
# green = randint(0, 255)
# blue = randint(0, 255)
# color(red, green, blue)

def randomcolour():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)


# shape("turtle")
# randomcolour()

def randomplace():
    penup()
    x = randint(-100, 100)
    y = randint(-100, 100)
    goto(x, y)
    pendown()


# shape("turtle")
# randomcolour()
# randomplace()
# stamp()
# randomcolour()
# randomplace()
# stamp()

def randomheading():
    degree = randint(1, 360)
    setheading(degree)


for i in range(30):
    randomcolour()
    randomplace()
    randomheading()
    stamp()
