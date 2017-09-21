# Filename: number_game_app.py
# Versions: Python 3
# A simple python programming app that showcases use of:
#	- lists
#	- loops
#	- functions
#	- user input
#	- importing libraries
#	- exceptions
# Features:
#	- receives number guess from user, validating if within 1-100
#	- tell user if hit or miss by comparing to secret number, give a hint if miss
#	- user tries maximum of 5 times
#   - user decides if wants to play a new game
import random

min = 1
max = 100

def show_hint(higher):
	if higher:
		print("Uh-oh. The secret number is something higher than that.")
	else:
		print("Uh-oh. The secret number is something lower than that.")

def new_game():
	secret_number = random.randint(min,max)
	tries = 1
	while 5 >= tries:
		guess = input("Give me a number from {}-{}: ".format(min,max))
		try:
			guess = int(guess)
		except ValueError:
			print("Oops.. {} is not a number. Please choose a number from {} to {}".format(guess,min,max))
			continue
		
		if secret_number == guess:
			print("Lucky man! You got it! Secret number is indeed: {}".format(secret_number))
			break
		elif (guess > max) or (guess < 1):
			print("Oops.. {} is not in range. Please choose a number from {} to {}".format(guess,min,max))
			continue
		
		if tries == 5:
			print("Oh snap! You ran out of tries!")
			print("The secret number was: {}".format(secret_number))
			break

		show_hint(secret_number > guess)
		print("You have {} more tries".format(5 - tries))		
		tries += 1
		
		
while True:
	new_game()
	if (input("Start a new game? [Y for new game, any other character to exit]") != "Y"):
		print("Bye now!")
		break
	

		

	
