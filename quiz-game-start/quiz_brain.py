class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        chosen_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False): ").lower()
        self.check_answer(chosen_answer, current_question.answer)

    def check_answer(self, chosen_answer, the_answer):
        if chosen_answer == the_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Wrong answer.")
        print(f"Correct answer was: {the_answer}")
        print(f"You're score is: {self.score}/{self.question_number}\n\n")




