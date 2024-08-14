from turtle import Turtle
BALL_WIDTH = 1
BALL_LENGTH = 1


class Ball(Turtle):

    def __init__(self, screensize):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=BALL_WIDTH, stretch_len=BALL_LENGTH)
        self.color("white")
        self.penup()
        self.screensize = screensize
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def refresh(self):
        self.setpos(0,0)
        self.move_speed = 0.1
        self.x_move *= -1


