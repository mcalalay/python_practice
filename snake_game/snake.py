from turtle import Turtle
import random
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.snake = []
        self.snake_builder()
        self.head = self.snake[0]

    def snake_builder(self):
        for position in START_POSITION:
            self.add_body(position)

    def add_body(self, position):
        snake_body = Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.snake.append(snake_body)

    def extend_body(self):
        self.add_body(self.snake[-1].position())

    def reset(self):
        for body in self.snake:
            body.goto(1000, 1000)
        self.snake.clear()
        self.snake_builder()
        self.head = self.snake[0]

    def move(self):
        for body_num in range(len(self.snake) - 1, 0, -1):
            (x, y) = self.snake[body_num - 1].pos()
            self.snake[body_num].goto(x, y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


