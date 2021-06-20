from turtle import Turtle, Screen
import random

turtle = Turtle()
colors = ["red", "orange", "blue", "green", "purple", "coral", "goldenrod", "lime", "black", "crimson"]
turtle_width = 10
turtle.width(turtle_width)
random_walk = False
step_count = 0


# random walk
def turtle_random_walk():
    turtle.color(random.choice(colors))
    random_number = [1, 2]
    if random.choice(random_number) == 1:
        turtle.lt(90)
    else:
        turtle.rt(90)
    turtle.forward(50)


while not random_walk:
    if step_count >= 100:
        random_walk = True
    else:
        turtle_random_walk()
        step_count += 1


screen = Screen()
screen.exitonclick()