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
		
def is_valid_guess(guess, guessed_hit, guessed_miss):
	if (not guess.isalpha()) or len(guess) != 1:
		print("That's not a valid guess.")
		return False
	elif(guess.lower() in guessed_hit + guessed_miss):
		print("You've given that already.")
		return False
	return True
	
def print_hits(word,hits):
	for letter in word:
		if letter in hits:
			print(letter, " ", end="")
		else:
			print("_", " ", end="")
	print()

def print_misses(misses,max_misses):
	print("Misses: {}/{}".format(len(misses),max_misses))
	for miss in misses:
		print(miss, " ", end="")
	print()
	
def player_wins(word, hits):
	return len(set(word)) == len(hits)

def new_game():
	list = populate_list()
	clear()
	word = random.choice(list)
	max_misses = int(len(word)/2)
	print(word) #debug line
	guessed_hit = []
	guessed_miss = []
	
	print("You got {} chances. Good luck!".format(max_misses))
	
	while len(guessed_miss) < max_misses:
		print_hits(word,guessed_hit)
		print_misses(guessed_miss,max_misses)
		guess = input("Give me a letter: ")
		
		if not is_valid_guess(guess, guessed_hit, guessed_miss):
			clear()
			continue
		clear()
		guess = guess.lower()
		if guess in word:
			guessed_hit.append(guess)
		else:
			guessed_miss.append(guess)
		
		if player_wins(word, guessed_hit):
			print("You guessed the word. Great! You win!")
			max_misses = -1
	else:
		print_hits(word,guessed_hit)
		if len(guessed_miss) == max_misses:
			print("You've run out of chances! The word was {}".format(word.upper()))
			print("You Lose!")
			
		if (input("Play again [Y-yes, anything else -no]?").lower() == "y"):
			guess
			new_game()
			
		print("Bye now!")
		sys.exit()
populate_list()
new_game()	
	
	
	