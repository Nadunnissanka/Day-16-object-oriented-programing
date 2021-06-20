from turtle import Screen
import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_rgb_color = (r, g, b)
    return random_rgb_color


turtle.color(random_color())

screen = Screen()
screen.exitonclick()