from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates = [-100, -60, -20, 20, 60, 100]
all_turtles = []
is_race_on = False

screen = Screen()
user_bet = screen.textinput(title="make a bet", prompt="what do you think, which turtle will win? enter the color")
screen.setup(width=500, height=400)

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_coordinates[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"you won! winner turtle is {winner}")
            else:
                print(f"you lost! winner turtle is {winner}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


# tom = Turtle(shape="turtle")
# tom.penup()
# tom.color(colors[1])
# tom.goto(x=-230, y=40)
#
# jim = Turtle(shape="turtle")
# jim.penup()
# jim.color(colors[2])
# jim.goto(x=-230, y=0)
#
# ben = Turtle(shape="turtle")
# ben.penup()
# ben.color(colors[3])
# ben.goto(x=-230, y=-40)
#
# kim = Turtle(shape="turtle")
# kim.penup()
# kim.color(colors[4])
# kim.goto(x=-230, y=-80)
#
# chris = Turtle(shape="turtle")
# chris.penup()
# chris.color(colors[5])
# chris.goto(x=-230, y=-120)


screen.exitonclick()
