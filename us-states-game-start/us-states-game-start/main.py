import turtle
import pandas as pd

font = ("Arial", 10, "normal")


screen = turtle.Screen()
bg = turtle.Turtle()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
bg.shape(image)


df = pd.read_csv("50_states.csv")
score = 0
game_on = True


def get_data(answer):
    for state in df.state:
        if answer.lower() == state.lower():
            x_cor = int(df.x[df.state == state])
            y_cor = int(df.y[df.state == state])
            print_answer(x_cor, y_cor, state)
            return True


def print_answer(x, y, state):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("black")
    pen.penup()
    pen.setpos(x, y)
    pen.write(state, font=font, align="center")


def countries_tracker(score, correct):
    if correct:
        score += 1
        return score


while game_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    print(answer_state)
    score = countries_tracker(score=score, correct=get_data(answer_state))
    if score == 50:
        game_on = False


turtle.mainloop()





