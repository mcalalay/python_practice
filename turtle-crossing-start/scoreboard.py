from turtle import Turtle
LEVEL_LOCATION = (-250, 250)
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.the_level()
        self.hideturtle()

    def the_level(self):
        self.goto(LEVEL_LOCATION)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def add_level(self):
        self.level += 1
        self.clear()
        self.the_level()

    def game_over(self):
        self.goto(-100, 0)
        self.write("GAME OVER!", align="left", font=FONT)