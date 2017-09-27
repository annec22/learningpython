from questions import Question
from questions import Add
from questions import Multiply
from quiz import Quiz

quizzie = Quiz(3, 10)

quizzie.take_quiz()

#for question in quizzie.questions:
#	print("Question: {}".format(question["question"]))
#	print("Answer: {}".format(question["answer"]))
#	print("Mark: {}".format(question["marks"]))
#	print("Time: {}".format(question["time_elapsed"]))
	