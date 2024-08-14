THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=350, background="#F9F5EB", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            fill=THEME_COLOR,
            font=FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=50, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.button_true = Button(image=self.true_img, highlightthickness=0, command=self.answer_true)
        self.button_false = Button(image=self.false_img, highlightthickness=0, command=self.answer_false)
        self.button_true.grid(row=2,column=0)
        self.button_false.grid(row=2, column=1)

        self.scoreboard = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="#F9F5EB", font=FONT)
        self.scoreboard.grid(row=0, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="#F9F5EB")
        if self.quiz.still_has_questions():
            self.scoreboard.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(text="You have reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")


    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
