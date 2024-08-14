import turtle as t
import random as rrr

tim = t.Turtle()

tim.shape("turtle")
tim.color("red")
#
# for i in range(16):
#     number_of_turns = 4
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)


# for i in range(50):
#     if i % 2 == 0:
#         timmy_the_turtle.down()
#         timmy_the_turtle.forward(10)
#     else:
#         timmy_the_turtle.up()
#         timmy_the_turtle.forward(10)


# def turn(number_of_turns):
#     counter = 0
#     for i in range(number_of_turns):
#         counter += 1
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/number_of_turns)
#         if counter == number_of_turns:
#             print("inside")
#             number_of_turns += 1
#             turn(number_of_turns)
#
#
# turn(3)

tim.speed("fastest")
t.colormode(255)


def color_creator():
    r = rrr.randint(0,255)
    g = rrr.randint(0, 255)
    b = rrr.randint(0, 255)
    return (r,g,b)


# def move_turtle(choices):
#     rrr.choice(choices)
#     tim.color(color_creator())
def draw(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(color_creator())
        tim.circle(150)
        tim.left(size_of_gap)
#     move_turtle([tim.right(rrr.choice([0,90,180,270])), tim.forward(20)])

draw(5)




screen = t.Screen()
screen.exitonclick()
