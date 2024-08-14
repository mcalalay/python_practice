from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.finish_line = FINISH_LINE_Y
        self.game_speed = 0.1

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def refresh(self):
        self.goto(STARTING_POSITION)
        self.game_speed *= 0.8

    def disappear(self):
        self.hideturtle()
        self.game_speed = 0.1

