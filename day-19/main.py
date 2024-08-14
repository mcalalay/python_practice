import turtle
from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]


is_race_on = False
screen = Screen()
screen.setup(width=1280, height=720)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.up()
    new_turtle.goto(x=-620, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 680:
            if user_bet == turtle.pencolor():
                print(f"You have won! The {turtle.pencolor()} turtle is the winning turtle!")
            else:
                print(f"You have lost! The {turtle.pencolor()} turtle is the winning turtle!")
            is_race_on = False

        turtle.forward(random.randint(0, 10))





screen.exitonclick()







# def move_forward():
#     new_turtle.forward(10)
#
#
# def move_backward():
#     new_turtle.backward(10)
#
#
# def counter_clock():
#     new_turtle.left(10)
#
#
# def clock():
#     new_turtle.right(10)
#
# def clean():
#     screen.resetscreen()
#
#
# screen.listen()
#
#
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="a", fun=counter_clock)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="d", fun=clock)
# screen.onkey(key="c", fun=clean)