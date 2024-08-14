from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
SCREEN_HEIGHT = screen.window_height()/2
SCREEN_WIDTH = screen.window_width()/2



screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.down, "s")

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_body()
        scoreboard.add_score()
        scoreboard.display_score()

    if snake.head.ycor() > SCREEN_HEIGHT or snake.head.ycor() < -SCREEN_HEIGHT \
            or snake.head.xcor() > SCREEN_WIDTH or snake.head.xcor() < -SCREEN_WIDTH:
        scoreboard.reset()
        snake.reset()

    for body in snake.snake[1:]:
        if snake.head.distance(body) < 10:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()