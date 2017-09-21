# Filename: number_game_app_v2.py
# Versions: Python 3
# Opposite of number_game_app.py. A simple python programming app that showcases use of:
#	- lists
#	- loops, use while-else
#	- functions, call function within itself
#	- user input
#	- importing libraries
#	- exceptions
# Features:
#	- receives a secret number from user, from 1 - 100
#	- tell computer if hit or miss by comparing to secret number and giving a clue
#	- computer tries maximum of 5 times
#   - user decides if wants to play a new game
#   - handle non-number input form user for secret number
#	- adjust guess from hint ([>]Too high? ot [<]Too low?, [any other character]Hit? : )
#	- detects cheaters

import random
max_tries = 3
def new_game(min,max):
	tries = 1
	secret_number = input("Give me a number from {} to {}: ".format(min,max))
	try:
		secret_number = int(secret_number)
	except ValueError:
		print("{} is not a number. I can't guess that.".format(secret_number))
	else:
		
		input("Press any key if you want me to guess now.")

		while max_tries >= tries:
			guess = random.randint(min,max)
			print("Guess[{}] is: {} ".format(tries,guess))
			hint = input("Is it [>]Too high?, [<]Too low? or [any other character]Hit? : ")
			if is_not_cheating(secret_number,guess,hint):		
				if hint == ">":
					max = guess-1
				elif hint == "<":
					min = guess+1
				else:
					print("Yeah. I know I'm smart. I can almost ready your mind.")
					break;
				tries+=1
			else:
				print("Hey! You're cheating!")
				break
		else:
			print("Oh snap! I've run out of tries. So your secret number was {}?? Okay, okay.".format(secret_number))
		
		
	if (input("Start a new game? [Y for new game, any other character to exit]") == "Y"):
		new_game(1,10)
	else:
		print("Bye now!")
	
def is_not_cheating(secret, guess, hint):
	if (secret > guess and hint == "<") or (secret < guess and hint == ">") or (secret ==guess and hint != "<" and hint !=">"):
		return True
	else:
		False
		
new_game(1,10)