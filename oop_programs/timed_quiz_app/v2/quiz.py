import random
import datetime

from questions import Add
from questions import Multiply
from questions import Subtract
from questions import Divide


class Quiz:


    def __init__(self, question_count=10, max_num=10):
        self.total_correct = 0
        self.time_elapsed = 0
        self.questions = []
        self.answers = []

        operations = (Add, Multiply, Subtract, Divide)
        for i in range(question_count):
            self.questions.append(random.choice(operations)(random.randint(1, max_num), random.randint(1, max_num)))

    def take_quiz(self):
        input("Press <ENTER> to start the {}-quesiton math quiz...".format(len(self.questions)))
        start = datetime.datetime.now()
        print("[{}] Start answering now!".format(start.strftime('%I:%M:%S:%f')))

        for question in self.questions:
            self.answers.append(self.ask(question))

        end = datetime.datetime.now()
        self.time_elapsed = round((end - start).total_seconds(), 2)
        print("[{}] Quiz is done!".format(end.strftime('%I:%M:%S:%f')))
        self.summary()

    def ask(self, question):
        question_start = datetime.datetime.now()
        answer = input("{}: ".format(question.text))
        try:
            answer = int(answer)
        except ValueError:
            pass

        question_end = datetime.datetime.now()
        result = (answer == question.answer)
        self.total_correct += result
        question_time_elapsed = (question_end - question_start).total_seconds()
        return answer, result, question_time_elapsed

    def summary(self):
        print('='*86)
        print('|{:^8}|{:^17}|{:^17}|{:^17}|{:^10}|{:^10}|'.format("Item", "Question", "Correct Answer", "Your Answer", "Time", "Mark"))
        print('=' * 86)
        for i in range(len(self.questions)):
            print("|{:^8}".format(i+1), end="")
            print("|{:^17}".format(self.questions[i].text), end="")
            print("|{:^17}".format(self.questions[i].answer), end="")
            print("|{:^17}".format(self.answers[i][0]), end="")
            print("|{:^10}".format(round(self.answers[i][2], 2)), end="")
            print("|{:^10}".format(self.answers[i][1]), end="|\n")
        print('='*86)
        print("Quiz Score: {}/{}".format(self.total_correct, len(self.questions)))
        print("Total Time: {} sconds".format(self.time_elapsed))
