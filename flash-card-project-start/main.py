from tkinter import *
import pandas as pd
import random

import pandas.errors

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
CSV_SAVED = "data/french_words.csv"
CSV_TO_LEARN = "data/remaining_words.csv"

window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.minsize(width=900, height=630)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, font=FONT_TITLE)
word_text = canvas.create_text(400, 263, font=FONT_WORD)
canvas.grid(row=0, column=0, columnspan=2)


def start():
    canvas.itemconfig(title_text, text="French")
    current_card = generate_word()
    canvas.itemconfig(word_text, text=current_card["French"])
    window.after(ms=3000, func=lambda word=current_card["English"]: reveal_answer(word))
    correct_button.grid(row=1, column=1)
    wrong_button.grid(row=1, column=0)
    start_button.grid_forget()


def reveal_answer(word):
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title_text, fill="white")
    canvas.itemconfig(word_text, fill="white")
    canvas.itemconfig(word_text, text=word)


def chose_correctly():
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title_text, fill="black")
    canvas.itemconfig(word_text, fill="black")
    current_card = generate_word()
    save_progress(current_card)
    canvas.itemconfig(word_text, text=current_card["French"])
    window.after(ms=3000, func=lambda word=current_card["English"]: reveal_answer(word))


def chose_wrong():
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title_text, fill="black")
    canvas.itemconfig(word_text, fill="black")
    current_card = generate_word()
    canvas.itemconfig(word_text, text=current_card["French"])
    window.after(ms=3000, func=lambda word=current_card["English"]: reveal_answer(word))



right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
correct_button = Button(image=right_img, command=chose_correctly)

wrong_button = Button(image=wrong_img, command=chose_wrong)


start_button = Button(text="Start", command=start, font=FONT_TITLE)
start_button.grid(row=1,column=0, columnspan=2)


#-------------------------------- READ Data ------------------------------------#

def read_data():
    try:
        df = pd.read_csv(CSV_TO_LEARN)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.read_csv(CSV_SAVED)
        data = df.to_dict(orient="records")
        print(data)
    else:
        data = df.to_dict(orient="records")
        print(data)
    return data


data = read_data()


def generate_word():
    if len(data) == 0:
        new_data = read_data()
        return random.choice(new_data)
    return random.choice(data)


def save_progress(current_card):
    data.remove(current_card)
    print(data)
    print("length::::::", len(data))
    if len(data) == 0:
        new_data = read_data()
        return random.choice(new_data)
    print(data)
    df = pd.DataFrame.from_dict(data)
    df.to_csv(CSV_TO_LEARN, index=False)
    return data



window.mainloop()



