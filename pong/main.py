from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600
screen = Screen()
screen.tracer(0)

screen.bgcolor("black")
screen.title("The Pong Game")
screen.setup(width=WIDTH, height=HEIGHT)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball(screensize=(WIDTH, HEIGHT))
scoreboard = Scoreboard()


screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() == (HEIGHT/2) - 20 or ball.ycor() == - ((HEIGHT/2) - 20):
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or \
            ball.distance(l_paddle) < 40 and ball.xcor() > -360:

        ball.bounce_x()

    if ball.xcor() == (WIDTH/2) - 20:
        ball.refresh()
        scoreboard.l_point()

    elif ball.xcor() == -((WIDTH/2) - 20):
        ball.refresh()
        scoreboard.r_point()



screen.exitonclick()