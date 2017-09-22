# Filename: letter_game_app.py
# Versions: Python 3
# A game similar to hangman. A simple python programming app that showcases use of:
#	- lists, list comprehension
#	- loops, use while-else
#	- functions, call function within itself
#	- user input
#	- importing libraries - random choice, os, sys
#	- str methods (is alpha)
#	- conditions (and or)
#	- open file, open(), and with
# Features:
#	- pick random word from a list or words
#	- draw spaces
#	- take letter guesses
#   - fill out spaces with correct guesses until solved or run out of chances
#   - handle non-number input form user for secret number
#	- prints misses
#	- prints win/lose
# 	- option to start a new game
#	- clear screen
#	- populate database from list of words
# To do's:
#	- organize into functions
#	- limit chances according to word length
import random
import os
import sys

def populate_list():
	with open('letter_game_app_words.txt') as f:
		read_data = [line.strip() for line in f]
	return read_data

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def new_game():
	list = populate_list()
	clear()
	max_misses = 5
	word = random.choice(list)
	print(word)
	guessed_hit = []
	guessed_miss = []
	
	while len(guessed_miss) < max_misses:
		guess = input("Give me a letter: ")
		
		if (not guess.isalpha()) or len(guess) != 1:	
			print("That's not a valid guess.")
			continue
		elif(guess in guessed_hit + guessed_miss):
			print("You've given that already.")
			continue
			
		if guess in word:
			guessed_hit.append(guess)
		else:
			guessed_miss.append(guess)
				
		for letter in word:
			if letter in guessed_hit:
				print(letter, " ", end="")
			else:
				print("_", " ", end="")
		print()
		
		print("Misses: ")
		for miss in guessed_miss:
			print(miss, " ", end="")
		print()
		
		if len(set(word)) == len(guessed_hit):
			print("You guessed the word. Great! You win!")
			max_misses = -1
	else:
		if len(guessed_miss) == max_misses:
			print("You've run out of chances! The word was {}".format(word))
			print("You Lose!")
		if (input("Play again [Y-yes, anything else -no]?") == "Y"):
			guess
			new_game()
			
		print("Bye now!")
		sys.exit()
populate_list()
new_game()	
	
	
	