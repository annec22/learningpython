# Filename: remove_vowels_app.py
# Versions: Python 3
# A script that removes the vowels from whatever words given:
#	- loops, use while-else
#	- functions, call function within itself
#	- user input
#	- exceptions
# Features:
#	- get word from user
#	- remove vowels

def disemvowel(word):
	word = list(word)
	vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
	
	for vowel in vowels:
		while True:
			try: 
				word.remove(vowel)
			except ValueError:
				break
				
	word = ''.join(word)
	return word

	
user_input = input("Give me a word, I'll disemvowel. \n>")

print("Here's your disemvoweled word: {}".format( disemvowel(user_input)))