from tkinter import *
from quiz_logic import QuizLogic

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizLogic):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # score label:
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # canvas/card:
        self.canvas = Canvas(width=300, height=250, bg="White", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20, padx=20)
        self.question_text = self.canvas.create_text(150, 125, text="Default Qustion Text Placeholder",
                                                     width=250, font=("Arial", 20, "italic"), fill=THEME_COLOR)

        # True:
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_selected)
        self.true_button.grid(row=2, column=0)

        # False:
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_selected)
        self.false_button.grid(row=2, column=1)

        self.get_next_q()
        self.window.mainloop()

    def get_next_q(self):
        """Gets next question and updates interface, if no question remains throws "END" card"""
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "END OF GAME")
            self.canvas.config(bg="white")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_selected(self):
        """True button selection checks answer"""
        correct = self.quiz.check_answer("True")
        self.feedback(correct)

    def false_selected(self):
        """False button selection checks answer"""
        correct = self.quiz.check_answer("False")
        self.feedback(correct)

    def feedback(self, correct):
        """Provides feedback to user by changing background and updating score"""
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_q)