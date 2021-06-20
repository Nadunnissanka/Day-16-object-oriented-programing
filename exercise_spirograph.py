import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)
turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_rgb_color = (r, g, b)
    return random_rgb_color


for _ in range(100):
    turtle.color(random_color())
    turtle.circle(50)
    turtle.tilt(10)
    current_heading = turtle.heading()
    turtle.setheading(current_heading + 10)

screen = t.Screen()
screen.exitonclick()