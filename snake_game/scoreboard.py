from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.hideturtle()
        self.color('white')
        self.setposition(0, (self.screen.window_height()/2)-20)
        self.display_score()

    def get_high_score(self):
        with open("data.txt", mode="r") as data:
            return int(data.read())

    def update_high_score(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.score))

    def display_score(self):
        self.clear()
        super().write(f"Score is {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.display_score()

    def add_score(self):
        self.score += 1
