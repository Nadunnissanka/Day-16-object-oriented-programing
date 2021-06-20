import random
import turtle as t

t.colormode(255)
turtle = t.Turtle()
turtle.penup()
turtle.hideturtle()

rgb_color_list = [(1, 12, 31), (54, 25, 17), (218, 127, 106), (9, 104, 160), (242, 213, 68), (150, 83, 39),
                  (216, 86, 63), (156, 6, 24), (165, 162, 30), (158, 62, 102), (207, 73, 103), (10, 64, 33),
                  (11, 96, 57), (95, 6, 20), (175, 134, 162), (7, 173, 217)]

turtle.setheading(225)
turtle.forward(250)
turtle.setheading(0)
for _ in range(10):
    for _ in range(10):
        turtle.dot(20, random.choice(rgb_color_list))
        turtle.forward(50)

    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(360)

screen = t.Screen()
screen.exitonclick()
