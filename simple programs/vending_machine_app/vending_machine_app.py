# Filename: vending_machine_app.py
# Versions: Python 3
# A simple program that lets users choose from chips, candies or sodas and gives them the item that is popped
#	- loops, use while
#	- user input
#	- exceptions
# Features:
#	- get choice from user
#	- gives snack
#	- handles if no more snack to be given from a specific category

sodas = ["Pepsi", "Coke", "Coke Zero", "Sprite", "Fanta", "Cali"]
chips = ["Doritos", "Fritos", "Cheetos", "Lays", "Combos"]
candies = ["Snickers", "KitKat", "m&ms", "Bueno", "Milka", "Cadburry"]

while True:
	choice = input("Would you like a SODA, some CHIPS, or a CANDY? \n>").lower()
	try:
		
		if choice == "soda":
			snack = sodas.pop()
		elif choice == "chips":
			snack = chips.pop()
		elif choice == "candy":
			snack = candies.pop()
		else:
			print("Sorry, no such things as that.")
			continue
	except IndexError:
		print("We're all out of {}. Sorry!".format(choice))
	else:
		print("Here's your {}: {}".format(choice, snack))