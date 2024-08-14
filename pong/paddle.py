from turtle import Turtle
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1


class Paddle(Turtle):

    def __init__(self, paddle_position):
        super().__init__()
        self.goto(paddle_position)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

