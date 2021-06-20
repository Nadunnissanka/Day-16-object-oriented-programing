from turtle import Turtle, Screen

turtle = Turtle()
colors = ["red", "orange", "blue", "green", "purple", "coral", "goldenrod", "lime", "black", "crimson"]



def draw_shapes():
    turtle_color_index = 0
    sides = 3
    angel = 120
    draw = False
    while not draw:
        for _ in range(sides):
            turtle.color(colors[turtle_color_index])
            turtle.left(angel)
            turtle.fd(100)
        turtle_color_index += 1
        sides += 1
        angel = 360 / sides

        if sides > 10:
            draw = True


draw_shapes()

screen = Screen()
screen.exitonclick()
