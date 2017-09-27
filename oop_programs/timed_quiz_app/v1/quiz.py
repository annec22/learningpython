import random
import datetime

from questions import Add
from questions import Multiply

class Quiz:
	questions = []
	
	def __init__(self, q_count=10, max_num=10):
		for i in range(q_count):
			if i < (q_count / 2):
				question = Add(random.randint(1, max_num), random.randint(1, max_num))
			else:
				question = Multiply(random.randint(1, max_num), random.randint(1, max_num))
			
			self.questions.append({"question":question.text, "answer":question.answer, "marks":None, "time_elapsed":None})
		
	def take_quiz(self):
		input("Press <ENTER> to start quiz...")
		time_now = datetime.datetime.now()
		print("[{}] Start answering now!".format(time_now.strftime('%I:%M:%S:%f')))
		
		for question in self.questions:
			marks, time_elapsed = self.ask(question)
			question["marks"] = marks
			question["time_elapsed"] = time_elapsed
		
		time_now = datetime.datetime.now()
		print("[{}] Quiz is done!".format(time_now.strftime('%I:%M:%S:%f')))
		self.summary()
		
	def ask(self, question):
		start = datetime.datetime.now()
		answer = int(input("{}: ".format(question["question"])))
		end = datetime.datetime.now()
		mark = (answer == question["answer"])
		time_elapsed = (end - start).total_seconds()
		return mark, time_elapsed
		
	def summary(self):
		correct_marks = 0
		total_time = 0
		for question in self.questions:
			correct_marks += question["marks"]
			total_time += question["time_elapsed"]
		
		print("Quiz Score: {}/{}".format(correct_marks, len(self.questions)))
		print("Total Time: {} sconds".format(round(total_time)))
	