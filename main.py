from turtle import *

# construct a object - Turtle
nadun = Turtle()
nadun.shape("turtle")
nadun.color("cyan")
nadun.fd(100)
nadun.rt(100)
nadun.fd(100)
nadun.lt(100)
nadun.fd(100)

# construct a object screen
my_screen = Screen()
my_screen.bgcolor("red")
my_screen.exitonclick()

# pretty table
from prettytable import PrettyTable

# constructing pretty table object
table = PrettyTable()

# using methods that are inside the object eg:- add_row()
table.field_name = ["Pokemon Name", "Type"]
table.add_row(["Pickachu", "Electric"])
table.add_row(["Bulbersur", "Grass/Poison"])
table.add_row(["Charizard", "Fire/Flying"])
table.add_row(["Weedle", "Bug"])

table.align = "l"

print(table)
